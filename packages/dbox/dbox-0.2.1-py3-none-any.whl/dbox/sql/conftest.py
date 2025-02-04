import pytest

from dbox.sql.ctx import SqlGenContext, set_sql_context


@pytest.fixture(scope="package")
def ctx():
    sql_ctx = SqlGenContext()
    with set_sql_context(sql_ctx):
        yield sql_ctx
