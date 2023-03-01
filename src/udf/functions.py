from snowflake.snowpark.functions import udf
from snowflake.snowpark.types import StringType


def combine(a: str, b: str) -> str:
    """
    A sample UDF implementation
    """
    return a+b
