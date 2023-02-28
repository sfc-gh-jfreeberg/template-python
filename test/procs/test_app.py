import pytest
import os

from snowflake.snowpark import Row
from src.util.local import LocalSession
from src.procs.app import run


@pytest.fixture
def local_session():
    return LocalSession().get_local_session()


@pytest.fixture(autouse=True)
def set_working_directory():
    # Sets the working directory to sources root so relative imports resolve properly
    os.chdir('src/')


def test_app_dim(local_session):
    expected_rows = 2
    expected_cols = 1
    
    df = run(local_session)
    n_col = len(df.columns)
    n_row = df.count()

    assert expected_rows == n_row
    assert expected_cols == n_col
