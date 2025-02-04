"""Drolta abstract syntax tree implementation.

"""

from __future__ import annotations

import dataclasses
import enum
import logging
from abc import ABC, abstractmethod
from typing import Any, Optional, cast

import antlr4
from drolta.parsing.DroltaLexer import DroltaLexer
from drolta.parsing.DroltaListener import DroltaListener
from drolta.parsing.DroltaParser import DroltaParser

_logger = logging.getLogger(__name__)


class ExpressionType(enum.IntEnum):
    """All expressions supported by drolta scripts."""

    PROGRAM = enum.auto()
    DECLARE_ALIAS = enum.auto()
    DECLARE_RULE = enum.auto()
    QUERY = enum.auto()
    ORDER_BY = enum.auto()
    GROUP_BY = enum.auto()
    LIMIT = enum.auto()
    PREDICATE_CALL = enum.auto()
    PREDICATE_NOT = enum.auto()
    VARIABLE = enum.auto()
    INT = enum.auto()
    FLOAT = enum.auto()
    STRING = enum.auto()
    BOOL = enum.auto()
    NULL = enum.auto()
    BINARY_LOGICAL_FILTER = enum.auto()
    COMPARISON_FILTER = enum.auto()
    MEMBERSHIP_FILTER = enum.auto()


_VALID_VALUE_EXPRESSIONS = (
    ExpressionType.INT,
    ExpressionType.FLOAT,
    ExpressionType.STRING,
    ExpressionType.BOOL,
    ExpressionType.NULL,
)
"""Subset of expression types used to represent values."""

_VALID_FILTER_EXPRESSIONS = (
    ExpressionType.BINARY_LOGICAL_FILTER,
    ExpressionType.COMPARISON_FILTER,
    ExpressionType.MEMBERSHIP_FILTER,
)
"""The subset of expression types used for filters."""

_VALID_WHERE_EXPRESSIONS = (
    ExpressionType.PREDICATE_CALL,
    ExpressionType.BINARY_LOGICAL_FILTER,
    ExpressionType.COMPARISON_FILTER,
    ExpressionType.MEMBERSHIP_FILTER,
)
"""The subset of expression types used in where clauses."""


class LogicalOp(enum.IntEnum):
    """Logical operators."""

    AND = enum.auto()
    OR = enum.auto()


class ComparisonOp(enum.IntEnum):
    """Comparison operators."""

    LT = enum.auto()
    GT = enum.auto()
    LTE = enum.auto()
    GTE = enum.auto()
    EQ = enum.auto()
    NEQ = enum.auto()


class ExpressionNode(ABC):
    """Abstract base class implemented by all AST Nodes."""

    @abstractmethod
    def get_expression_type(self) -> ExpressionType:
        """Return the type of this expression."""
        raise NotImplementedError()


def is_filter_expression(node: ExpressionNode) -> bool:
    """Check if the given node is a valid filter expression."""

    return node.get_expression_type() in _VALID_FILTER_EXPRESSIONS


def is_where_expression(node: ExpressionNode) -> bool:
    """Check if a given node is a valid where expression."""

    return node.get_expression_type() in _VALID_WHERE_EXPRESSIONS


def is_value_expression(node: ExpressionNode) -> bool:
    """Check if a given node is a valid value expression."""

    return node.get_expression_type() in _VALID_VALUE_EXPRESSIONS


class ProgramNode(ExpressionNode):
    """The root node of Drolta ASTs."""

    __slots__ = ("children",)

    children: list[ExpressionNode]

    def __init__(self, children: list[ExpressionNode]) -> None:
        super().__init__()
        self.children = children

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.PROGRAM


class DeclareAliasExpression(ExpressionNode):
    """Expression node for declaring new predicate aliases."""

    __slots__ = ("original_name", "alias")

    original_name: str
    alias: str

    def __init__(self, original_name: str, alias: str) -> None:
        super().__init__()
        self.original_name = original_name
        self.alias = alias

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.DECLARE_ALIAS


class DeclareRuleExpression(ExpressionNode):
    """Expression node for declaring new rules."""

    __slots__ = ("name", "params", "where_expressions")

    name: str
    params: list[
        tuple[
            str,
            str,
        ]
    ]
    where_expressions: list[ExpressionNode]

    def __init__(
        self,
        name: str,
        params: list[tuple[str, str]],
        where_expressions: list[ExpressionNode],
    ) -> None:
        super().__init__()
        self.name = name
        self.params = params
        self.where_expressions = where_expressions

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.DECLARE_RULE


class BinaryExpression(ExpressionNode, ABC):
    """Abstract base class implemented by all binary operator expressions."""

    __slots__ = ("left", "right")

    left: ExpressionNode
    right: ExpressionNode

    def __init__(self, left: ExpressionNode, right: ExpressionNode) -> None:
        super().__init__()
        self.left = left
        self.right = right


class NotFilterExpression(ExpressionNode):
    """Logical NOT filter expressions."""

    __slots__ = ("expr",)

    expr: ExpressionNode

    def __init__(self, expr: ExpressionNode) -> None:
        super().__init__()
        self.expr = expr

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.BINARY_LOGICAL_FILTER


class BinaryLogicalFilterExpression(BinaryExpression):
    """Logical AND/OR filter expressions."""

    __slots__ = ("op",)

    op: LogicalOp

    def __init__(
        self, left: ExpressionNode, right: ExpressionNode, op: LogicalOp
    ) -> None:
        super().__init__(left, right)
        self.op = op

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.BINARY_LOGICAL_FILTER

    def __str__(self) -> str:
        if self.op == LogicalOp.AND:
            return f"({self.left} AND {self.right})"
        else:
            return f"({self.left} OR {self.right})"


class ComparisonFilterExpression(BinaryExpression):
    """Comparison filter expressions."""

    __slots__ = ("op",)

    op: ComparisonOp

    def __init__(
        self, left: ExpressionNode, right: ExpressionNode, op: ComparisonOp
    ) -> None:
        super().__init__(left, right)
        self.op = op

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.COMPARISON_FILTER

    def __str__(self) -> str:
        if self.op == ComparisonOp.GT:
            return f"({self.left} > {self.right})"
        elif self.op == ComparisonOp.LT:
            return f"({self.left} < {self.right})"
        elif self.op == ComparisonOp.GTE:
            return f"({self.left} >= {self.right})"
        elif self.op == ComparisonOp.LTE:
            return f"({self.left} <= {self.right})"
        elif self.op == ComparisonOp.EQ:
            return f"({self.left} = {self.right})"
        else:
            return f"({self.left} != {self.right})"


class MembershipFilterExpression(ExpressionNode):
    """Membership checking filter expression."""

    __slots__ = ("expr", "values")

    expr: ExpressionNode
    values: list[ExpressionNode]

    def __init__(self, expr: ExpressionNode, values: list[ExpressionNode]) -> None:
        super().__init__()
        self.expr = expr
        self.values = values

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.MEMBERSHIP_FILTER

    def __str__(self) -> str:
        value_list = ", ".join(str(v) for v in self.values)
        return f"({self.expr} in [{value_list}])"


class PredicateExpression(ExpressionNode):
    """A predicate expression."""

    __slots__ = ("name", "params")

    name: str
    params: list[tuple[str, ExpressionNode]]

    def __init__(self, name: str, params: list[tuple[str, ExpressionNode]]) -> None:
        super().__init__()
        self.name = name
        self.params = params

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.PREDICATE_CALL


class VariableExpression(ExpressionNode):
    __slots__ = ("variable",)

    variable: str

    def __init__(self, variable: str) -> None:
        super().__init__()
        self.variable = variable

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.VARIABLE

    def __str__(self) -> str:
        return f"{self.variable[1:]}"


class IntExpression(ExpressionNode):
    """An integer expression"""

    __slots__ = ("value",)

    value: int

    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.INT

    def __str__(self) -> str:
        return f"{self.value}"


class FloatExpression(ExpressionNode):
    """An float expression"""

    __slots__ = ("value",)

    value: float

    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = value

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.FLOAT

    def __str__(self) -> str:
        return f"{self.value}"


class StringExpression(ExpressionNode):
    """A string expression"""

    __slots__ = ("value",)

    value: str

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.STRING

    def __str__(self) -> str:
        return f"{self.value}"


class BoolExpression(ExpressionNode):
    """A boolean expression"""

    __slots__ = ("value",)

    value: bool

    def __init__(self, value: bool) -> None:
        super().__init__()
        self.value = value

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.BOOL

    def __str__(self) -> str:
        return f"{self.value}"


class NullExpression(ExpressionNode):
    """A null expression"""

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.NULL

    def __str__(self) -> str:
        return "NULL"


class NotPredicateExpression(ExpressionNode):
    """Not predicate expression."""

    __slots__ = ("expr",)

    expr: ExpressionNode

    def __init__(self, expr: ExpressionNode) -> None:
        super().__init__()
        self.expr = expr

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.PREDICATE_NOT


class QueryExpression(ExpressionNode):
    """A query expression."""

    __slots__ = ("params", "where_expressions", "order_by", "group_by", "limit")

    params: list[
        tuple[
            str,
            str,
        ]
    ]
    where_expressions: list[ExpressionNode]
    order_by: Optional[OrderByExpression]
    group_by: Optional[GroupByExpression]
    limit: Optional[OrderByExpression]

    def __init__(
        self,
        params: list[tuple[str, str]],
        where_expressions: list[ExpressionNode],
        order_by: Optional[OrderByExpression] = None,
        group_by: Optional[GroupByExpression] = None,
        limit: Optional[OrderByExpression] = None,
    ) -> None:
        super().__init__()
        self.params = params
        self.where_expressions = where_expressions
        self.order_by = order_by
        self.group_by = group_by
        self.limit = limit

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.QUERY


class OrderByExpression(ExpressionNode):
    """Order by expression."""

    __slots__ = ("expr",)

    expr: ExpressionNode

    def __init__(self, expr: ExpressionNode) -> None:
        super().__init__()
        self.expr = expr

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.ORDER_BY

    def __str__(self) -> str:
        return f"ORDER BY {self.expr}"


class GroupByExpression(ExpressionNode):
    """Group by expression."""

    __slots__ = ("expr",)

    expr: ExpressionNode

    def __init__(self, expr: ExpressionNode) -> None:
        super().__init__()
        self.expr = expr

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.GROUP_BY

    def __str__(self) -> str:
        return f"GROUP BY {self.expr}"


class LimitExpression(ExpressionNode):
    """Limit expression."""

    __slots__ = ("value",)

    value: int

    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def get_expression_type(self) -> ExpressionType:
        return ExpressionType.LIMIT

    def __str__(self) -> str:
        return f"LIMIT {self.value}"


class ASTVisitor(ABC):
    """Abstract base class implemented by visitors that traverse ASTs."""

    @abstractmethod
    def visit_program(self, node: ProgramNode) -> None:
        """Visit Program Node."""
        raise NotImplementedError()

    @abstractmethod
    def visit_declare_alias(self, node: DeclareAliasExpression) -> None:
        """Visit DeclareAliasNode."""
        raise NotImplementedError()

    @abstractmethod
    def visit_declare_rule(self, node: DeclareRuleExpression) -> None:
        """Visit DeclareRuleNode."""
        raise NotImplementedError()

    @abstractmethod
    def visit_query(self, node: QueryExpression) -> None:
        """Visit QueryExpression."""
        raise NotImplementedError()

    def visit(self, node: ExpressionNode) -> None:
        """Dynamic dispatch by node type."""
        expression_type = node.get_expression_type()

        if expression_type == ExpressionType.PROGRAM:
            return self.visit_program(cast(ProgramNode, node))

        if expression_type == ExpressionType.DECLARE_ALIAS:
            return self.visit_declare_alias(cast(DeclareAliasExpression, node))

        if expression_type == ExpressionType.DECLARE_RULE:
            return self.visit_declare_rule(cast(DeclareRuleExpression, node))

        if expression_type == ExpressionType.QUERY:
            return self.visit_query(cast(QueryExpression, node))

        raise TypeError(f"Unsupported node expression type: {expression_type.name}")


@dataclasses.dataclass(slots=True)
class _ListenerScope:
    """A scope of data used within the script listener."""

    rule_name: str = ""
    rule_params: list[tuple[str, str]] = dataclasses.field(default_factory=list)
    expr_queue: list[ExpressionNode] = dataclasses.field(default_factory=list)
    predicate_params: list[tuple[str, ExpressionNode]] = dataclasses.field(
        default_factory=list
    )
    post_processing_expr_list: list[ExpressionNode] = dataclasses.field(
        default_factory=list
    )
    order_by: Optional[OrderByExpression] = None
    group_by: Optional[GroupByExpression] = None
    limit: Optional[OrderByExpression] = None


class _ScriptListener(DroltaListener):
    """Customize listener for drolta scripts."""

    __slots__ = ("_ast", "_scope_stack")

    _scope_stack: list[_ListenerScope]
    _ast: ExpressionNode

    def __init__(self) -> None:
        self._scope_stack = []
        self._ast = ProgramNode([])

    def get_ast(self) -> ExpressionNode:
        """Get the generated AST."""
        return self._ast

    def enterProg(self, ctx: DroltaParser.ProgContext):
        self._scope_stack.append(_ListenerScope())

    def exitProg(self, ctx: DroltaParser.ProgContext):
        scope = self._scope_stack.pop()

        self._ast = ProgramNode(scope.expr_queue)

    def exitAlias_declaration(self, ctx: DroltaParser.Alias_declarationContext):
        original_name = str(ctx.original.text)  # type: ignore
        alias_name = str(ctx.alias.text)  # type: ignore

        self._scope_stack[-1].expr_queue.append(
            DeclareAliasExpression(original_name, alias_name)
        )

    def enterRule_declaration(self, ctx: DroltaParser.Rule_declarationContext):
        self._scope_stack.append(_ListenerScope())

    def exitRule_declaration(self, ctx: DroltaParser.Rule_declarationContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            DeclareRuleExpression(
                name=scope.rule_name,
                params=scope.rule_params,
                where_expressions=scope.expr_queue,
            )
        )

    def exitDefine_clause(self, ctx: DroltaParser.Define_clauseContext):
        rule_name = ctx.IDENTIFIER().getText()  # type: ignore
        params = [(v.getText(), "") for v in ctx.VARIABLE()]  # type: ignore

        self._scope_stack[-1].rule_name = rule_name
        self._scope_stack[-1].rule_params = params

    def enterQuery(self, ctx: DroltaParser.QueryContext):
        self.new_scope()

    def exitQuery(self, ctx: DroltaParser.QueryContext):
        scope = self.pop_scope()

        expr = QueryExpression(
            params=scope.rule_params,
            where_expressions=scope.expr_queue,
            order_by=scope.order_by,
            group_by=scope.group_by,
            limit=scope.limit,
        )

        self._scope_stack[-1].expr_queue.append(expr)

    def exitFind_clause(self, ctx: DroltaParser.Find_clauseContext):
        for v in ctx.VARIABLE():  # type: ignore
            self._scope_stack[-1].rule_params.append((v.getText(), ""))  # type: ignore

    def exitOrder_by_statement(self, ctx: DroltaParser.Order_by_statementContext):
        self._scope_stack[-1].order_by = OrderByExpression(
            VariableExpression(ctx.VARIABLE().getText())  # type: ignore
        )

    def exitGroup_by_statement(self, ctx: DroltaParser.Group_by_statementContext):
        self._scope_stack[-1].group_by = GroupByExpression(
            VariableExpression(ctx.VARIABLE().getText())  # type: ignore
        )

    def exitLimit_statement(self, ctx: DroltaParser.Limit_statementContext):
        self._scope_stack[-1].limit = LimitExpression(
            int(ctx.INT_LITERAL().getText())  # type: ignore
        )

    def enterPredicate(self, ctx: DroltaParser.PredicateContext):
        self._scope_stack.append(_ListenerScope())

    def exitPredicate(self, ctx: DroltaParser.PredicateContext):
        predicate_name: str = ctx.IDENTIFIER().getText()  # type: ignore

        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            PredicateExpression(name=predicate_name, params=scope.predicate_params)  # type: ignore
        )

    def enterPredicateNot(self, ctx: DroltaParser.PredicateNotContext):
        self._scope_stack.append(_ListenerScope())

    def exitPredicateNot(self, ctx: DroltaParser.PredicateNotContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            NotPredicateExpression(scope.expr_queue[0])
        )

    def enterPredicate_param(self, ctx: DroltaParser.Predicate_paramContext):
        self._scope_stack.append(_ListenerScope())

    def exitPredicate_param(self, ctx: DroltaParser.Predicate_paramContext):
        scope = self._scope_stack.pop()

        atom = scope.expr_queue[0]

        self._scope_stack[-1].predicate_params.append(
            (ctx.IDENTIFIER().getText(), atom)  # type: ignore
        )

    def enterComparisonFilter(self, ctx: DroltaParser.ComparisonFilterContext):
        self._scope_stack.append(_ListenerScope())

    def exitComparisonFilter(self, ctx: DroltaParser.ComparisonFilterContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            ComparisonFilterExpression(
                op=_ScriptListener.parse_comparison_op(ctx.op.getText()),  # type: ignore
                left=VariableExpression(ctx.left.text),  # type: ignore
                right=scope.expr_queue[0],
            )
        )

    def enterAndFilter(self, ctx: DroltaParser.AndFilterContext):
        self._scope_stack.append(_ListenerScope())

    def exitAndFilter(self, ctx: DroltaParser.AndFilterContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            BinaryLogicalFilterExpression(
                op=LogicalOp.AND, left=scope.expr_queue[0], right=scope.expr_queue[1]
            )
        )

    def enterOrFilter(self, ctx: DroltaParser.OrFilterContext):
        self._scope_stack.append(_ListenerScope())

    def exitOrFilter(self, ctx: DroltaParser.OrFilterContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            BinaryLogicalFilterExpression(
                op=LogicalOp.OR, left=scope.expr_queue[0], right=scope.expr_queue[1]
            )
        )

    def enterNotFilter(self, ctx: DroltaParser.NotFilterContext):
        self._scope_stack.append(_ListenerScope())

    def exitNotFilter(self, ctx: DroltaParser.NotFilterContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            NotFilterExpression(
                expr=scope.expr_queue[0],
            )
        )

    def enterInFilter(self, ctx: DroltaParser.InFilterContext):
        self._scope_stack.append(_ListenerScope())

    def exitInFilter(self, ctx: DroltaParser.InFilterContext):
        scope = self._scope_stack.pop()

        self._scope_stack[-1].expr_queue.append(
            MembershipFilterExpression(
                expr=VariableExpression(ctx.VARIABLE().getText()),  # type: ignore
                values=scope.expr_queue,
            )
        )

    def exitAtom(self, ctx: DroltaParser.AtomContext):
        if ctx.VARIABLE():
            self._scope_stack[-1].expr_queue.append(
                VariableExpression(ctx.VARIABLE().getText())  # type: ignore
            )
            return

        if ctx.INT_LITERAL():
            self._scope_stack[-1].expr_queue.append(
                IntExpression(int(ctx.INT_LITERAL().getText()))  # type: ignore
            )
            return

        if ctx.FLOAT_LITERAL():
            self._scope_stack[-1].expr_queue.append(
                FloatExpression(float(ctx.FLOAT_LITERAL().getText()))  # type: ignore
            )
            return

        if ctx.STRING_LITERAL():
            self._scope_stack[-1].expr_queue.append(
                StringExpression(str(ctx.STRING_LITERAL().getText()))  # type: ignore
            )
            return

        if ctx.BOOLEAN_LITERAL():  # type: ignore
            if ctx.FLOAT_LITERAL().getText() == "TRUE":  # type: ignore
                self._scope_stack[-1].expr_queue.append(BoolExpression(True))
            else:
                self._scope_stack[-1].expr_queue.append(BoolExpression(False))
            return

        if ctx.NULL():
            self._scope_stack[-1].expr_queue.append(NullExpression())

    def new_scope(self):
        self._scope_stack.append(_ListenerScope())

    def pop_scope(self) -> _ListenerScope:
        return self._scope_stack.pop()

    @staticmethod
    def parse_comparison_op(text: str) -> ComparisonOp:
        """Convert text to a comparison operation"""
        if text == "=":
            return ComparisonOp.EQ
        if text == "!=":
            return ComparisonOp.NEQ
        if text == "<=":
            return ComparisonOp.LTE
        if text == "<":
            return ComparisonOp.LT
        if text == ">=":
            return ComparisonOp.GTE
        if text == ">":
            return ComparisonOp.GT

        raise ValueError(f"Unrecognized comparison operator: '{text}'.")


def generate_ast(script_text: str) -> ExpressionNode:
    """Generate a Drolta AST from the given script text."""

    input_stream = antlr4.InputStream(script_text)
    lexer = DroltaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = DroltaParser(stream)
    error_listener = _SyntaxErrorListener()

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)  # type: ignore

    tree = parser.prog()

    if error_listener.error_count:
        error_message = "Syntax errors found in drolta script:\n"
        for msg in error_listener.error_messages:
            error_message += msg + "\n"

        _logger.error(error_message)

        raise SyntaxError(error_message)

    listener = _ScriptListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)  # type: ignore

    drolta_ast = listener.get_ast()

    return drolta_ast


class _SyntaxErrorListener(antlr4.DiagnosticErrorListener):
    __slots__ = ("error_count", "error_messages")

    error_count: int
    error_messages: list[str]

    def __init__(self) -> None:
        super().__init__()
        self.error_count = 0
        self.error_messages = []

    def syntaxError(
        self,
        recognizer: Any,
        offendingSymbol: Any,
        line: int,
        column: int,
        msg: str,
        e: Any,
    ) -> None:
        self.error_count += 1
        self.error_messages.append(f"line {line}:{column} {msg}")

    def clear(self) -> None:
        """Clear all cached errors."""
        self.error_count = 0
        self.error_messages.clear()
