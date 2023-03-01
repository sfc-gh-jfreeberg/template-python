# Python Project Template for Snowflake

Use this project template to start writing data applications on Snowflake using Python.

## Start Here

### Prerequisites

To develop your applications locally, you will need

- A Snowflake account
- Python 3.8
- An IDE or code editor (VS Code, PyCharm, etc.)

### Set Credentials

Set your account URL, username, role, database, and schema in [app.toml](app.toml).

Next, set an environment variable with your Snowflake password:

```bash
# Linux/MacOS
set SNOWSQL_PASSWORD=<your-password>
```

```bash
# Windows
$env:SNOWSQL_PASSWORD = <your-password>
```

Optional: You can set this env var permanently by editing your bash profile (on Linux/MacOS) or 
using the System Properties menu (on Windows).

### Install dependencies

Set up a virtual environment using [Anaconda](), [Miniconda](), or [virtualenv](). For example, the following command will create and activate a virtual environment named `venv`:

```
python3 -m venv venv
source venv/bin/activate
```

Next, import the packages in [requirements.txt](requirements.txt):

```
pip install -r requirements.txt
```

### Test connection

Once you've set your credentials and installed the packages, you can test your connection to Snowflake by executing the stored procedure in [`app.py`](src/procs/app.py):

```
cd src
python procs/app.py
```

You should see output like this:

```
------------------------------------------------------
|Hello world                                         |
------------------------------------------------------
|Welcome to Snowflake!                               |
|Learn more: https://www.snowflake.com/snowpark/     |
------------------------------------------------------
```

### Run tests

You can run the test suite locally from the project root:

```
python -m pytest
```

### Deploy to Snowflake

#### Deploy locally

1. Install snmow cli
1. `snow connection add` from project root
1. `snow login` from project root
1. `snow configure` 

#### Deploy from CI Pipeline

The GitHub Actions [workflow file](.github/workflows/build-and-deploy.yml) allows you to continously deploy your objects to Snowflake. When you're ready,
create a secret in your GitHub repository named `SNOWSQL_PASSWORD` with your account password. Then, replace the placeholders in the [workflow file](.github/workflows/build-and-deploy.yml)
with your username, database, and other account information.

Once you do that, your project contents will be deployed to Snowflake every time a commit is pushed to your GitHub repository.

## Project Structure

- [procs/](src/procs/): Directory for stored procedures
- [udf/](src/udf/): Directory for your user-defined functions
- [util/](src/util/): Directory for methods/classes shared between UDFs and procedures


## Docs

- [Snowpark Developer Guide for Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)
- [Creating Stored Procedures](https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-sprocs)
- [Snowpark API Reference](https://docs.snowflake.com/developer-guide/snowpark/reference/python/index.html)
