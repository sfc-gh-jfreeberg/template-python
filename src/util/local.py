from snowflake.snowpark.session import Session
import tomli
import os


class LocalSession:

    def get_local_session(self) -> Session:
        toml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../app.toml'))

        try:
            pwd = os.environ['SNOWSQL_PWD']

            with open(toml_path, 'rb') as f:
                conn = tomli.load(f)['dev']

                return Session.builder.configs({
                    'account': conn['accountname'],
                    'user': conn['username'],
                    'password': pwd,
                    'database': conn['database'],
                    'schema': conn['schema'],
                    'role': conn['role'],
                    'warehouse': conn['warehouse']
                }).create()
                
        except KeyError as e:
            print('ERROR: Environment variable, SNOWSQL_PASSWORD, not found. Please set this variable.')
            raise e
