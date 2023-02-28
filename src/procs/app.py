from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import (col, DataFrame)
from snowflake.snowpark.types import StringType


def run(session: Session) -> DataFrame:
    """
    A sample stored procedure which creates a small DataFrame and prints it to the console.
    """

    from src.udf.functions import combine
    session.add_import(path='../src/udf/functions.py', import_path='src.udf.functions')

    schema = ['col_1', 'col_2']

    data = [
        ("Welcome to ", "Snowflake!"), 
        ("Learn more: ", "https://www.snowflake.com/snowpark/")]

    df = session.create_dataframe(data, schema)
    combine = session.udf.register(combine, return_type=StringType())

    df2 = df.select(
        combine(
            col('col_1'),
            col('col_2')
        ).as_('Hello world')
    ).sort('Hello world', ascending=False)

    df2.show()
    return df2


if __name__ == '__main__':
    """
    This entrypoint is used for local development, and creates a session object from app.toml
    """

    import sys, os
    sys.path.insert(0, '..')  # Necessary to import from local directory

    from src.util.local import LocalSession
    session = LocalSession().get_local_session()

    run(session)
