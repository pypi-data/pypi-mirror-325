import pytest
from pyconn.db.kdb import KDB, Server


@pytest.fixture
def db():
    server = Server()
    server.name = "TEST"
    server.host = "127.0.0.1"
    server.port = 9900
    server.username = ""
    server.password = ""
    server.pandas = False
    return server


def test_kdb_conn(db):
    q = KDB(server=db)
    result = q.query_sync("{1+1}[]")
    assert result == 2


def test_kdb_query_with_parameters(db):
    q = KDB(server=db)
    result = q.query_sync("{x+y}", 1, 2)
    assert result == 3
