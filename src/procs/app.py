"""
An example stored procedure. __main__ provides an entrypoint for local development
and testing.
"""

import os

from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import col, DataFrame
from snowflake.snowpark.functions import call_udf


def run(snowpark_session: Session) -> str:
    """
    A sample stored procedure which creates a small DataFrame, prints it to the
    console, and returns the number of rows in the table.
    """

    schema = ["col_1", "col_2"]

    data = [
        ("Welcome to ", "Snowflake!"),
        ("Learn more: ", "https://www.snowflake.com/snowpark/"),
    ]

    df: DataFrame = snowpark_session.create_dataframe(data, schema)

    df2 = df.select(
        call_udf("combine", col("col_1"), col("col_2")).as_("Hello world")
    ).sort("Hello world", ascending=False)

    df2.show()
    return df2.count()


if __name__ == "__main__":
    # This entrypoint is used for local development, and creates a session object from app.toml

    import sys

    sys.path.insert(0, "..")  # Necessary to import from local directory

    # Create connection from toml
    from src.util.local import get_env_var_config

    p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../app.toml"))
    session = Session.builder.configs(get_env_var_config()).create()

    run(session)
