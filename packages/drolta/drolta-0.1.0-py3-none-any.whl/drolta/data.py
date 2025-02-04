"""Drolta Data Classes.

"""

from __future__ import annotations

import dataclasses
import sqlite3

from drolta.ast import ExpressionNode


@dataclasses.dataclass(slots=True)
class RuleData:
    """A Drolta query rule."""

    name: str
    params: list[tuple[str, str]]
    where_expressions: list[ExpressionNode]


@dataclasses.dataclass(slots=True)
class EngineData:
    """Holds all the data managed by the engine."""

    db: sqlite3.Connection
    result: sqlite3.Cursor
    aliases: dict[str, str] = dataclasses.field(default_factory=dict)
    rules: dict[str, RuleData] = dataclasses.field(default_factory=dict)
    temp_table_names: list[str] = dataclasses.field(default_factory=list)
