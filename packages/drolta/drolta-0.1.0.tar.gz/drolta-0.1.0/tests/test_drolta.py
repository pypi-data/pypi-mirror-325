"""Unit Tests of Drolta.

This test files does not use pytest fixtures because the database connection
needs to be closed at the end of each test. There is probably a more elegant
way to handle this (probably with a context manager). However, this works for
now.

"""

import sqlite3

import drolta
import drolta.engine
from drolta.interpreter import has_alias_cycle


def initialize_test_data(db: sqlite3.Connection) -> None:
    """Initializes the provided data"""

    cursor = db.cursor()

    cursor.executescript(
        """
        DROP TABLE IF EXISTS characters;
        DROP TABLE IF EXISTS houses;
        DROP TABLE IF EXISTS relations;

        CREATE TABLE characters (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT,
            house_id INTEGER,
            sex TEXT,
            life_stage TEXT,
            is_alive INTEGER,
            FOREIGN KEY (house_id) REFERENCES houses(id)
        ) STRICT;

        CREATE TABLE houses (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            reputation INT NOT NULL,
            is_noble INT NOT NULL
        ) STRICT;

        CREATE TABLE relations (
            from_id INTEGER NOT NULL,
            to_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            FOREIGN KEY (from_id) REFERENCES characters(id),
            FOREIGN KEY (to_id) REFERENCES characters(id)
        ) STRICT;
        """
    )

    cursor.executemany(
        """
        INSERT INTO
        characters (id, name, house_id, sex, life_stage, is_alive)
        VALUES
        (?, ?, ?, ?, ?, ?);
        """,
        [
            (1, "Rhaenyra", 1, "F", "Adult", 1),
            (2, "Laenor", 2, "M", "Adult", 1),
            (3, "Harwin", 3, "M", "Adult", 1),
            (4, "Jacaerys", 2, "M", "Teen", 1),
            (5, "Addam", None, "M", "Teen", 1),
            (6, "Corlys", 2, "M", "Adult", 1),
            (7, "Marilda", None, "F", "Adult", 0),
            (8, "Alyn", None, "M", "Adult", 1),
            (9, "Rhaenys", 1, "F", "Adult", 0),
            (10, "Laena", 2, "F", "Adult", 0),
            (11, "Daemon", 1, "M", "Adult", 1),
            (12, "Baela", 1, "F", "Teen", 1),
            (13, "Viserys", 1, "M", "Senior", 0),
            (14, "Alicent", 5, "F", "Adult", 1),
            (15, "Otto", 5, "M", "Senior", 1),
            (16, "Aegon", 1, "M", "Teen", 1),
            (17, "Cristen", 4, "M", "Adult", 1),
        ],
    )

    cursor.executemany(
        """
        INSERT INTO
            houses(id, name, reputation, is_noble)
        VALUES
            (?, ?, ?, ?);
        """,
        [
            (1, "Targaryen", 50, 1),
            (2, "Velaryon", 50, 1),
            (3, "Strong", 50, 0),
            (4, "Cole", 50, 0),
            (5, "Hightower", 50, 1),
            (6, "Belmont", 50, 1),
        ],
    )

    cursor.executemany(
        """
        INSERT INTO
            relations (from_id, to_id, type)
        VALUES
            (?, ?, ?);
        """,
        [
            (4, 1, "Mother"),  # Jace -> Rhaenyra
            (4, 2, "Father"),  # Jace -> Laenor
            (4, 3, "BiologicalFather"),  # Jace -> Harwin
            (5, 6, "BiologicalFather"),  # Addam -> Corlys
            (2, 6, "BiologicalFather"),  # Laenor -> Corlys
            (2, 6, "Father"),  # Laenor -> Corlys
            (5, 7, "Mother"),  # Addam -> Marilda
            (8, 7, "Mother"),  # Alyn -> Marilda
            (8, 6, "BiologicalFather"),  # Alyn -> Corlys
            (2, 9, "Mother"),  # Laenor -> Rhaenys
            (10, 9, "Mother"),  # Laena -> Rhaenys
            (10, 6, "Father"),  # Laena -> Corlys
            (10, 6, "BiologicalFather"),  # Laena -> Corlys
            (6, 9, "Widower"),  # Corlys -> Rhaenys
            (6, 9, "FormerSpouse"),  # Corlys -> Rhaenys
            (9, 6, "FormerSpouse"),  # Rhaenys -> Corlys
            (12, 10, "Mother"),  # Baela -> Laena
            (12, 11, "Father"),  # Baela -> Daemon
            (12, 11, "BiologicalFather"),  # Baela -> Daemon
            (1, 11, "Spouse"),  # Rhaenyra -> Daemon
            (11, 1, "Spouse"),  # Daemon -> Rhaenyra
            (10, 11, "FormerSpouse"),  # Laena -> Daemon
            (11, 10, "FormerSpouse"),  # Daemon -> Laena
            (11, 10, "Widower"),  # Daemon -> Laena
            (1, 13, "Father"),  # Rhaenyra -> Viserys
            (1, 13, "BiologicalFather"),  # Rhaenyra -> Viserys
            (16, 14, "Mother"),  # Aegon -> Alicent
            (14, 15, "Father"),  # Alicent => Otto
            (14, 15, "BiologicalFather"),  # Alicent => Otto
        ],
    )

    db.commit()


def test_define_predicate_alias() -> None:
    """Ensure table aliases are registered and properly used."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    engine.execute_script(
        """
        ALIAS characters as Character;
        """
    )

    result = engine.execute(
        """
        FIND ?x
        WHERE
            Character(?x, family="Targaryen");
        """
    ).fetchall()

    # TODO: Add assert statement for an expected number of rows.

    db.close()


def test_define_rule_alias() -> None:
    """Ensure rule aliases and registered and properly used."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    engine.execute_script(
        """
        ALIAS FromNobleFamily as IsNobility;

        DEFINE
            FromNobleFamily(?x)
        WHERE
            characters(id=?x, family_id=?family_id)
            family(id=?family_id, is_noble=TRUE);
        """
    )

    result = engine.execute(
        """
        FIND ?x
        WHERE
            IsNobility(?x);
        """
    ).fetchall()

    # TODO: Add assert statement for an expected number of rows.

    db.close()


def test_define_rule() -> None:
    """Ensure rules can be defined and used within a query."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    engine.execute_script(
        """
        DEFINE
            FromNobleFamily(?x)
        WHERE
            characters(id=?x, family_id=?family_id)
            family(id=?family_id, is_noble=TRUE);
        """
    )

    result = engine.execute(
        """
        FIND ?x
        WHERE
            FromNobleFamily(?x);
        """
    ).fetchall()

    # TODO: Add assert statement for an expected number of rows.

    db.close()


def test_composite_rules() -> None:
    """Test composing a rule using other rules."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    engine.execute_script(
        """
        DEFINE
            IsVampire(?x)
        WHERE
            traits(character_id=?x, trait="Vampire");

        DEFINE
            FromNobleFamily(?x)
        WHERE
            characters(id=?x, family_id=?family_id)
            family(id=?family_id, is_noble=TRUE);

        DEFINE
            NobleVampire(?x)
        WHERE
            IsVampire(?x)
            FromNobleFamily(?x);
        """
    )

    result = engine.execute(
        """
        FIND ?x
        WHERE
            NobleVampire(?x);
        """
    ).fetchall()

    # TODO: Add assert statements for an expected number of rows

    db.close()


def test_single_predicate_query() -> None:
    """Test queries composed of a single predicate."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND ?x
        WHERE
            Character(?x, family="Targaryen");
        """
    ).fetchall()

    # TODO: Add assert statement for an expected number of rows.

    db.close()


def test_query_output_aliases() -> None:
    """Test that queries output columns with the proper alias names."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND ?x AS character_id
        WHERE
            Character(?x, family="Targaryen");
        """
    ).fetchall()

    # TODO: Add assert statement for an expected number of rows.

    db.close()


def test_rule_param_aliases() -> None:
    """Test that rule parameters can be referred to using provided aliases."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    engine.execute_script(
        """
        DEFINE
            FromNobleFamily(?x AS character_id)
        WHERE
            characters(id=?x, family_id=?family_id)
            family(id=?family_id, is_noble=TRUE);
        """
    )

    result = engine.execute(
        """
        FIND ?x
        WHERE
            FromNobleFamily(?x);
        """
    ).fetchall()

    # TODO: Add assert statement for an expected number of rows.

    db.close()


def test_multi_predicate_query() -> None:
    """Test a query that joins across multiple predicate statements."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND
            ?x
        WHERE
            characters(id=?x, family_id=?family_id)
            family(id=?family_id, is_noble=TRUE);
        """
    ).fetchall()

    # TODO: Add assert statements for an expected number of rows

    db.close()


def test_eq_filter() -> None:
    """Test the equals comparison filter."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND
            ?x
        WHERE
            characters(id=?x, life_stage=?life_stage, family_id=?family_id)
            family(id=?family_id, name="Targaryen")
            (?life_stage = "Adult");
        """
    ).fetchall()

    # TODO: Add assert statements for an expected number of rows

    db.close()


def test_neq_filter() -> None:
    """Test the not equals filter."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND
            ?x
        WHERE
            characters(id=?x, life_stage=?life_stage, family_id=?family_id)
            family(id=?family_id, name="Targaryen")
            (?life_stage != "Adult");
        """
    ).fetchall()

    # TODO: Add assert statements for an expected number of rows

    db.close()


def test_lt_filter() -> None:
    """Test the less than filter."""


def test_gt_filter() -> None:
    """Test the greater than filter."""


def test_lte_filter() -> None:
    """Test the less-than or equal to filter."""


def test_gte_filter() -> None:
    """Test the greater-than or equal to filter."""


def test_membership_filter() -> None:
    """Test the list membership filter."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND
            ?x
        WHERE
            characters(id=?x, life_stage=?life_stage, family_id=?family_id)
            family(id=?family_id, name=?family_name)
            (?family_name IN ["Belmont", "Targaryen"]);
        """
    ).fetchall()

    # TODO: Add assert statements for an expected number of rows

    db.close()


def test_null_check() -> None:
    """Test checking for NULL values."""

    db = sqlite3.Connection(":memory:")

    initialize_test_data(db)

    engine = drolta.engine.QueryEngine(db)

    result = engine.execute(
        """
        FIND
            ?x
        WHERE
            characters(id=?x, family_id=NULL);
        """
    ).fetchall()

    # TODO: Add assert statements for an expected number of rows

    db.close()


def test_and_statement() -> None:
    """Test using AND keyword to combine filter statements."""


def test_or_statement() -> None:
    """Test using OR keyword to combine filter statements."""


def test_not_filter_statement() -> None:
    """Test using NOT keyword on filter statements."""


def test_not_predicate_statement() -> None:
    """Test using NOT keyword on predicate statements."""


def test_not_rule_statement() -> None:
    """Test using NOT keyword on rule statements."""


def test_alias_cycle_detection() -> None:
    """Test that alias cycles are detected."""

    aliases = {"A": "D", "B": "C", "G": "D", "E": "A", "F": "B"}

    assert has_alias_cycle(aliases) == (False, "")

    aliases["C"] = "F"

    assert has_alias_cycle(aliases) == (True, "B")
