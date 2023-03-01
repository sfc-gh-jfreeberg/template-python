
CREATE STAGE IF NOT EXISTS artifacts;

PUT file://*.zip @artifacts AUTO_COMPRESS=FALSE OVERWRITE=TRUE;

CREATE OR REPLACE PROCEDURE helloWorldProcedure()
    RETURNS integer
    LANGUAGE PYTHON
    RUNTIME_VERSION = 3.8
    IMPORTS = ('@artifacts/my-project.zip')
    HANDLER = 'src.procs.app.run'
    PACKAGES = ('pytest','snowflake-snowpark-python','tomli','toml')
    ;

CREATE OR REPLACE FUNCTION combine(a String, b String)
    RETURNS String
    LANGUAGE PYTHON
    RUNTIME_VERSION = 3.8
    IMPORTS = ('@artifacts/my-project.zip')
    HANDLER = 'src.udf.functions.combine'
    PACKAGES = ('pytest','snowflake-snowpark-python','tomli','toml')
    ;