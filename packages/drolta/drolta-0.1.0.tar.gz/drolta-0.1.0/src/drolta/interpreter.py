"""Drolta Interpreter."""

from __future__ import annotations

import dataclasses
import enum
import logging
from typing import cast

from drolta.ast import (
    ASTVisitor,
    DeclareAliasExpression,
    DeclareRuleExpression,
    ExpressionNode,
    ExpressionType,
    NotPredicateExpression,
    PredicateExpression,
    ProgramNode,
    QueryExpression,
    is_filter_expression,
)
from drolta.data import EngineData, RuleData
from drolta.errors import ProgrammingError

_logger = logging.getLogger(__name__)


def get_execution_order(node: ExpressionNode) -> int:
    """Get the order number of the expression (Lower is higher priority)."""
    expression_type = node.get_expression_type()

    if expression_type == ExpressionType.PREDICATE_CALL:
        return 0

    if is_filter_expression(node):
        return 1

    if expression_type == ExpressionType.PREDICATE_NOT:
        return 1

    return 2


def cycle_check_dfs(
    aliases: dict[str, str], value: str, visited: set[str], stack: list[str]
) -> tuple[bool, str]:
    if value not in visited:
        visited.add(value)
        stack.append(value)

        if value in aliases:
            target = aliases[value]

            if target not in visited:
                result = cycle_check_dfs(aliases, target, visited, stack)
                if result[0] is True:
                    return result

            if target in stack:
                return True, target

    stack.pop()
    return False, ""


def has_alias_cycle(aliases: dict[str, str]) -> tuple[bool, str]:
    """Check if the alias dictionary has a cycle."""

    stack: list[str] = []
    visited: set[str] = set()

    for alias in aliases.keys():
        if alias not in visited:
            result = cycle_check_dfs(aliases, alias, visited, stack)
            if result[0] is True:
                return result

    return False, ""


@dataclasses.dataclass(frozen=True, slots=True)
class TempResult:
    """Information about an intermediate result of a query."""

    table_name: str
    """The name of the temporary table with this result's data"""
    output_vars: set[str]
    """The column names of the temp table"""

    @staticmethod
    def get_common_vars(b: TempResult, a: TempResult) -> list[str]:
        """Get common variables between two temp results."""
        return sorted(a.output_vars.intersection(b.output_vars))


@dataclasses.dataclass(slots=True)
class Scope:
    """Information about the current variable scope of the query."""

    scope_id: int
    """The ID of the current scope."""
    output_vars: list[tuple[str, str]] = dataclasses.field(default_factory=list)
    """Variables output by this scope."""
    tables: list[TempResult] = dataclasses.field(default_factory=list)
    """Temporary result tables."""
    next_table_id: int = 1
    """The ID assigned to the next table in this scope."""


class InterpreterMode(enum.IntEnum):
    """Various Interpreter Modes."""

    SCRIPT_EVAL = 0
    """Only allows for declaration operations."""
    QUERY_EVAL = 1
    """Only allows for query operations."""


class Interpreter(ASTVisitor):
    """Interpreter used for scripts."""

    TEMP_TABLE_PREFIX = "temp__"
    """Name prefix for all temporary tables created by the query engine."""

    __slots__ = ("engine_data", "mode", "scope_stack")

    engine_data: EngineData
    """State data for the query engine."""
    mode: InterpreterMode
    """Current interpreter mode."""
    scope_stack: list[Scope]
    """Stack of scopes used during query evaluation."""

    def __init__(
        self,
        engine_data: EngineData,
        mode: InterpreterMode = InterpreterMode.SCRIPT_EVAL,
    ) -> None:
        super().__init__()
        self.engine_data = engine_data
        self.mode = mode
        self.scope_stack = []

    def visit_declare_alias(self, node: DeclareAliasExpression):
        if self.mode == InterpreterMode.QUERY_EVAL:
            raise ProgrammingError("Alias declarations not allowed while querying.")

        new_alias_dict = {**self.engine_data.aliases, node.alias: node.original_name}

        has_cycle, cycled_alias = has_alias_cycle(new_alias_dict)

        if has_cycle:
            raise ProgrammingError(f"Circular aliases for: {cycled_alias}.")

        self.engine_data.aliases[node.alias] = node.original_name

        _logger.debug("Declared alias: %s -> %s", node.alias, node.original_name)

    def visit_declare_rule(self, node: DeclareRuleExpression):
        if self.mode == InterpreterMode.QUERY_EVAL:
            raise ProgrammingError("Rule declarations not allowed while querying.")

        rule = RuleData(
            name=node.name,
            params=[*node.params],
            where_expressions=[*node.where_expressions],
        )

        self.engine_data.rules[rule.name] = rule

        _logger.debug("Declared rule: %s", rule.name)

    def visit_query(self, node: QueryExpression):
        if self.mode == InterpreterMode.SCRIPT_EVAL:
            raise ProgrammingError("Queries not allowed while loading scripts.")

        self.scope_stack.clear()

        # This is where the magic will happen.
        _logger.debug("Evaluating query.")

        # Create a new base scope
        scope = self.new_scope()
        # Remove the "?" prefix from output params
        scope.output_vars = [(var_name[1:], alias) for var_name, alias in node.params]

        # Sort expressions to push filters and not-predicate expressions
        # to the end of the query.
        where_expressions = sorted(node.where_expressions, key=get_execution_order)

        for expr in where_expressions:
            expression_type = expr.get_expression_type()

            if expression_type == ExpressionType.PREDICATE_CALL:
                self.dispatch_visit_predicate(cast(PredicateExpression, expr))

            elif is_filter_expression(expr):
                self.visit_filter(expr)

            elif expression_type == ExpressionType.PREDICATE_NOT:
                self.visit_not_predicate(cast(NotPredicateExpression, expr))

            self._attempt_join_latest_table()

        self._force_join_all_tables()

        result_table = self.get_scope().tables[-1]

        # For the end of the query, we want to select from the result table
        # all the variables in output vars and assign them to any aliases

        output_cols: list[str] = []
        for var_name, alias in self.get_scope().output_vars:
            if alias:
                output_cols.append(f"{var_name} AS {alias}")
            else:
                output_cols.append(str(var_name))

        sql_statement = (
            "SELECT DISTINCT\n"
            f"\t{', '.join(output_cols)}\n"
            "FROM\n"
            f"\t{result_table.table_name}\n"
        )

        if node.order_by:
            sql_statement += f"{node.order_by}\n"

        if node.group_by:
            sql_statement += f"{node.group_by}\n"

        if node.limit:
            sql_statement += f"{node.limit}\n"

        sql_statement += ";"

        _logger.debug("Calculating Final Output:\n%s", sql_statement)

        cursor = self.engine_data.db.cursor()

        result = cursor.execute(sql_statement)

        self.engine_data.result = result

    def visit_program(self, node: ProgramNode):
        for child in node.children:
            self.visit(child)

    def visit_rule(self, name: str, node: PredicateExpression):
        current_scope = self.new_scope()

        output_vars: list[str] = []
        for _, expr in node.params:
            if expr.get_expression_type() == ExpressionType.VARIABLE:
                output_vars.append(str(expr))

        rule = self.engine_data.rules[name]

        # Sort expressions to push filters and not-predicate expressions
        # to the end of the query.
        where_expressions = sorted(rule.where_expressions, key=get_execution_order)

        for expr in where_expressions:
            expression_type = expr.get_expression_type()

            if expression_type == ExpressionType.PREDICATE_CALL:
                self.dispatch_visit_predicate(cast(PredicateExpression, expr))

            elif is_filter_expression(expr):
                self.visit_filter(expr)

            elif expression_type == ExpressionType.PREDICATE_NOT:
                self._force_join_all_tables()
                self.visit_not_predicate(cast(NotPredicateExpression, expr))

            self._attempt_join_latest_table()

        self._force_join_all_tables()

        result_table = current_scope.tables[-1]

        self.pop_scope()

        # Perform a select over the result table using the output vars
        sql_statement = self.get_predicate_select_expr(
            result_table.table_name, node.params
        )

        table_name = self.get_temp_table_name()

        sql_temp_table_statement = (
            f"CREATE TEMPORARY TABLE {table_name} AS\n" f"{sql_statement}"
        )

        _logger.debug("Calculating Rule Output:\n%s", sql_temp_table_statement)

        cursor = self.engine_data.db.cursor()

        cursor.execute(sql_temp_table_statement)

        self.engine_data.db.commit()

        self.get_scope().tables.append(
            TempResult(table_name=table_name, output_vars=set(output_vars))
        )

    def dispatch_visit_predicate(self, node: PredicateExpression):
        """Manages visiting predicates as true predicates or rules."""

        predicate_name = self.get_final_predicate_name(node.name)

        if predicate_name in self.engine_data.rules:
            self.visit_rule(predicate_name, node)
        else:
            self.visit_predicate(predicate_name, node)

    def visit_predicate(self, name: str, node: PredicateExpression):
        """Evaluate predicate expression against a table in the database."""

        current_scope = self.get_scope()

        output_vars: list[str] = []
        for _, expr in node.params:
            if expr.get_expression_type() == ExpressionType.VARIABLE:
                output_vars.append(str(expr))

        # This is assumed to be a sqlite table
        # SQLite will throw an error if it is not
        sql_statement = Interpreter.get_predicate_select_expr(name, node.params)

        table_name = self.get_temp_table_name()

        sql_temp_table_statement = (
            f"CREATE TEMPORARY TABLE {table_name} AS\n" f"{sql_statement}"
        )

        _logger.debug("Executing predicate select:\n%s", sql_temp_table_statement)

        cursor = self.engine_data.db.cursor()

        cursor.execute(sql_temp_table_statement)

        self.engine_data.db.commit()

        current_scope.tables.append(
            TempResult(table_name=table_name, output_vars=set(output_vars))
        )

    def visit_filter(self, node: ExpressionNode):
        """Evaluate predicate expression."""

        # This function forces all the previous tables to join and performs a filter
        # on them.
        self._force_join_all_tables()

        result_table = self.get_scope().tables[-1]

        sql_statement = (
            "SELECT\n"
            "\t*\n"
            "FROM\n"
            f"\t{result_table.table_name}\n"
            "WHERE\n"
            f"\n{node}"
        )

        table_name = self.get_temp_table_name()

        new_result_table = TempResult(
            table_name=table_name, output_vars=set(result_table.output_vars)
        )

        sql_temp_table_statement = (
            f"CREATE TEMPORARY TABLE {table_name} AS\n" f"{sql_statement};"
        )

        _logger.debug("Filtering Output:\n%s", sql_temp_table_statement)

        cursor = self.engine_data.db.cursor()

        cursor.execute(sql_temp_table_statement)

        # delete the old temp_table
        cursor.execute(f"DROP TABLE IF EXISTS {result_table.table_name};")

        self.engine_data.db.commit()

        self.get_scope().tables.pop()

        self.get_scope().tables.append(new_result_table)

    def visit_not_predicate(self, node: NotPredicateExpression):
        """Evaluate predicate expression."""

        self.new_scope()

        expression_type = node.expr.get_expression_type()

        if expression_type == ExpressionType.PREDICATE_CALL:
            self.dispatch_visit_predicate(cast(PredicateExpression, node.expr))

        else:
            raise ProgrammingError("Not statement expects a predicate or rule.")

        result_table = self.get_scope().tables[-1]

        self.pop_scope()

        last_table = self.get_scope().tables[-1]

        table_name = self.get_temp_table_name()

        not_join_result = TempResult(
            table_name=table_name, output_vars=set(last_table.output_vars)
        )

        shared_vars = TempResult.get_common_vars(last_table, result_table)

        if shared_vars:
            where_filters = " AND ".join(
                f"({result_table.table_name}.{v} = {last_table.table_name}.{v})"
                for v in shared_vars
            )

            sql_statement = (
                "SELECT\n"
                "\t*\n"
                "FROM\n"
                f"\t{last_table.table_name}\n"
                "WHERE\n"
                "\tNOT EXISTS (\n"
                "\t\tSELECT\n"
                "\t\t\t1\n"
                "\t\tFROM\n"
                f"\t\t\t{result_table.table_name}\n"
                "\t\tWHERE\n"
                f"\t\t\t{where_filters}"
                ")"
            )

            sql_temp_table_statement = (
                f"CREATE TEMPORARY TABLE {table_name} AS\n" f"{sql_statement};\n"
            )

            _logger.debug("Joining Not Join:\n%s", sql_temp_table_statement)

            cursor = self.engine_data.db.cursor()

            cursor.execute(sql_temp_table_statement)

            cursor.execute(f"DROP TABLE IF EXISTS {result_table.table_name};")

            cursor.execute(f"DROP TABLE IF EXISTS {last_table.table_name}")

            self.engine_data.db.commit()

            self.get_scope().tables.pop()

            self.get_scope().tables.append(not_join_result)

    def _force_join_all_tables(self) -> None:
        """Force all tables in the scope to join."""

        current_scope = self.get_scope()

        if len(current_scope.tables) > 1:
            last_table = current_scope.tables[-1]

            # Create a large join under a new temp_table.

            sql_join_statement = (
                "SELECT\n" "*\n" "FROM\n" f"\t{last_table.table_name}\n"
            )

            output_vars: set[str] = set(last_table.output_vars)

            num_other_tables = len(current_scope.tables) - 1
            for table_idx, other_table in enumerate(current_scope.tables[:-1]):
                shared_vars = TempResult.get_common_vars(last_table, other_table)

                output_vars = output_vars.union(other_table.output_vars)

                if shared_vars:
                    join_cols = " AND ".join(
                        f"({other_table.table_name}.{v} = {last_table.table_name}.{v})"
                        for v in shared_vars
                    )

                    sql_join_statement += (
                        f"JOIN {other_table.table_name} ON {join_cols}"
                    )
                else:
                    sql_join_statement += f"CROSS JOIN {other_table.table_name}"

                if table_idx == num_other_tables - 1:
                    sql_join_statement += ";"

                sql_join_statement += "\n"

            table_name = self.get_temp_table_name()

            sql_temp_table_statement = (
                f"CREATE TEMPORARY TABLE {table_name} AS\n" f"{sql_join_statement}"
            )

            _logger.debug("Joining All Tables:\n%s", sql_temp_table_statement)

            cursor = self.engine_data.db.cursor()

            cursor.execute(sql_temp_table_statement)

            # Remove all tables involved with the join
            for table in current_scope.tables:
                cursor.execute(f"DROP TABLE IF EXISTS {table.table_name};")

            current_scope.tables.clear()

            self.engine_data.db.commit()

            current_scope.tables.append(
                TempResult(table_name=table_name, output_vars=output_vars)
            )

    def _attempt_join_latest_table(self) -> None:
        """Try to join the latest table with any existing ones."""
        current_scope = self.get_scope()
        if len(current_scope.tables) > 1:
            # Check if the last table has common vars with any
            # of the previous tables
            last_table = current_scope.tables[-1]

            shared_table_indexes: set[int] = set()
            output_vars: set[str] = set(last_table.output_vars)
            have_shared: list[tuple[int, list[str]]] = []
            for table_idx, other_table in enumerate(current_scope.tables[:-1]):
                shared_vars = TempResult.get_common_vars(last_table, other_table)
                if shared_vars:
                    have_shared.append((table_idx, shared_vars))
                    shared_table_indexes.add(table_idx)
                    output_vars = output_vars.union(other_table.output_vars)

            if have_shared:
                # Create a large join under a new temp_table.

                sql_join_statement = (
                    "SELECT\n" "*\n" "FROM\n" f"\t{last_table.table_name}\n"
                )

                for idx, var_names in have_shared:
                    temp_table = current_scope.tables[idx]

                    join_cols = " AND ".join(
                        f"({temp_table.table_name}.{v} = {last_table.table_name}.{v})"
                        for v in var_names
                    )

                    sql_join_statement += (
                        f"JOIN {temp_table.table_name} ON {join_cols}\n"
                    )

                table_name = self.get_temp_table_name()

                sql_temp_table_statement = (
                    f"CREATE TEMPORARY TABLE {table_name} AS\n" f"{sql_join_statement}"
                )

                _logger.debug("Joining Tables:\n%s", sql_temp_table_statement)

                cursor = self.engine_data.db.cursor()

                cursor.execute(sql_temp_table_statement)

                # Remove all tables involved with the join
                for idx in range(len(current_scope.tables), -1, -1):
                    if (
                        idx == len(current_scope.tables) - 1
                        or idx in shared_table_indexes
                    ):
                        table = current_scope.tables.pop(idx)

                        cursor.execute(f"DROP TABLE IF EXISTS {table.table_name};")

                self.engine_data.db.commit()

                current_scope.tables.append(
                    TempResult(table_name=table_name, output_vars=output_vars)
                )

    @staticmethod
    def get_predicate_select_expr(
        name: str, params: list[tuple[str, ExpressionNode]]
    ) -> str:
        """Generate a SQLite SELECT expression from the predicate data."""

        variable_params: list[tuple[str, str]] = []
        where_params: list[tuple[str, str]] = []
        for column_name, expr in params:
            if expr.get_expression_type() == ExpressionType.VARIABLE:
                variable_params.append((column_name, str(expr)))
            else:
                where_params.append((column_name, str(expr)))

        column_aliases = ", ".join(
            f'{col} AS "{var_name}"' for col, var_name in variable_params
        )

        if where_params:
            where_filters = " AND ".join(f"{col}={val}" for col, val in where_params)

            select_expr = (
                "SELECT\n"
                f"\t{column_aliases}\n"
                "FROM\n"
                f"\t{name}\n"
                "WHERE\n"
                f"\t{where_filters};\n"
            )
        else:
            select_expr = "SELECT\n" f"\t{column_aliases}\n" "FROM\n" f"\t{name};\n"

        return select_expr

    def get_final_predicate_name(self, name: str) -> str:
        """Resolve the final name of a predicate from a potential alias."""

        final_name = name

        while final_name in self.engine_data.aliases:
            final_name = self.engine_data.aliases[final_name]

        return final_name

    def get_temp_table_name(self) -> str:
        """Generate a name for the next temporary table."""
        current_scope = self.get_scope()

        table_name = (
            self.TEMP_TABLE_PREFIX
            + f"{current_scope.scope_id}_"
            + str(current_scope.next_table_id)
        )

        current_scope.next_table_id += 1

        return table_name

    def get_scope(self) -> Scope:
        """Get the current scope."""
        return self.scope_stack[-1]

    def new_scope(self) -> Scope:
        """Push a new scope on the stack."""
        if self.scope_stack:
            scope = Scope(scope_id=self.scope_stack[-1].scope_id + 1)
        else:
            scope = Scope(scope_id=0)

        self.scope_stack.append(scope)
        return scope

    def pop_scope(self) -> Scope:
        """Pop the current scope."""
        return self.scope_stack.pop()
