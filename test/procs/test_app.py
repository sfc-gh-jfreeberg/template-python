import pytest
import os

from snowflake.snowpark import Row
from src.util.local import get_dev_config
from src.procs.app import run
from snowflake.snowpark.session import Session


@pytest.fixture
def local_session():
    p = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../app.toml'))
    return Session.builder.configs(get_dev_config("dev", p)).create() 


@pytest.fixture(autouse=True)
def set_working_directory():
    # Sets the working directory to sources root so relative imports resolve properly
    os.chdir('src/')


def test_app_dim(local_session):
    expected_n_rows = 2
    actual_n_rows = run(local_session)
    assert expected_n_rows == actual_n_rows
