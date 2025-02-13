import pytest
from pyconn.db.qpool import Query, Server


@pytest.fixture
def db1():
    server = Server()
    server.name = "TEST1"
    server.host = "127.0.0.1"
    server.port = 9900
    server.username = "dm"
    server.password = "dmonetree"
    server.pandas = False
    return server


@pytest.fixture
def db2():
    server = Server()
    server.name = "TEST2"
    server.host = "127.0.0.1"
    server.port = 9800
    server.username = ""
    server.password = ""
    server.pandas = False
    return server


def test_pool_conn(db1):
    q1 = Query(db1)
    result1 = q1.query_sync("{1+1}[]")
    assert result1 == 2
