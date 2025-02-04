"""Drolta Query Engine.

"""

from __future__ import annotations

import logging
import sqlite3

from drolta.ast import generate_ast
from drolta.data import EngineData
from drolta.interpreter import Interpreter, InterpreterMode

_logger = logging.getLogger(__name__)


class QueryEngine:
    """
    A QueryEngine manages user-defined content and handles queries to SQLite.

    Parameters
    ----------
    db : sqlite3.Connection
        A SQlite database Connection.
    """

    __slots__ = ("_data", "_interpreter")

    _data: EngineData
    _interpreter: Interpreter

    def __init__(self, db: sqlite3.Connection) -> None:
        self._data = EngineData(db, db.cursor())
        self._interpreter = Interpreter(self._data)

    def execute_script(self, drolta_script: str) -> None:
        """Load rules and aliases from a Drolta script.

        Parameters
        ----------
        drolta_script : str
            Drolta script text containing rule and alias definitions.
        """
        self.clear_cache()

        _logger.debug("Generating drolta AST.")

        drolta_ast = generate_ast(drolta_script)

        _logger.debug("Executing drolta script.")

        self._interpreter.mode = InterpreterMode.SCRIPT_EVAL
        self._interpreter.visit(drolta_ast)

        return

    def execute(self, drolta_query: str) -> sqlite3.Cursor:
        """Query the SQLite database and return a cursor to the results.

        Parameters
        ----------
        drolta_query : str
            Text defining a Drolta query.
        """

        self.clear_cache()

        _logger.debug("Generating drolta AST.")

        drolta_ast = generate_ast(drolta_query)

        _logger.debug("Executing drolta query.")

        self._interpreter.mode = InterpreterMode.QUERY_EVAL
        self._interpreter.visit(drolta_ast)

        return self._data.result

    def clear_cache(self) -> None:
        """Clear all the query engine's cashed data and temporary tables."""

        # self._clear_scopes()
        # self._clear_last_result()

    # def _clear_last_result(self) -> None:
    #     """Delete the table with the last result."""
    #     if self._last_result is None:
    #         return
    #
    #     cursor = self._db.cursor()
    #
    #     cursor.execute(f"""DROP TABLE IF EXISTS {self._last_result.table_name}""")
    #
    #     self._db.commit()
    #
    #     self._last_result = None
    #
    # def _clear_scopes(self) -> None:
    #     """Remove all temporary tables from existing scopes."""
    #
    #     cursor = self._db.cursor()
    #
    #     while self._scope_stack:
    #         scope = self._scope_stack.pop()
    #
    #         for table_name in scope.tables:
    #             cursor.execute(f"""DROP TABLE IF EXISTS {table_name}""")
    #
    #         scope.tables.clear()
    #
    #     self._db.commit()
