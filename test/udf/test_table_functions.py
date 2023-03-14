import os
import pytest
from snowflake.snowpark.session import Session
from src.util.local import get_env_var_config
from src.udf.table_functions import CostByCategory_TF
from snowflake.snowpark.types import (
    IntegerType,
    StructType,
    StructField,
    StringType,
    FloatType,
)
from snowflake.snowpark.functions import udtf


# @pytest.fixture(autouse=True)
# def set_working_directory():
#     # Sets the working directory to sources root so relative imports resolve properly
#     os.chdir('src/')


# @pytest.fixture
# def local_session() -> Session:
#     return Session.builder.configs(get_env_var_config()).create()


# def test_udtf(local_session: Session):

#     # Register UDTF
#     local_session.add_import(path='../src/udf/table_functions.py', import_path='src.udf.table_functions')
#     o_schema = StructType([StructField("category", StringType()), StructField("cost", FloatType())])
#     test_tf = udtf(CostByCategory_TF, output_schema=o_schema, input_types=[StringType(), IntegerType(), FloatType()], session=local_session)

#     # Create test data
#     schema = StructType([StructField("category", StringType()), StructField("quantity", IntegerType()), StructField("price", FloatType())])
#     df = local_session.create_dataframe([
#         ("A", 1, 5.0),
#         ("A", 2, 2.0),
#         ("B", 1, 0.0),
#         ("B", 5, 1.0),
#         ("C", 1, 1.0)], schema)

#     # Call UDTF
#     df2 = local_session.table_function("test_udf", df)
#     df2.show()
