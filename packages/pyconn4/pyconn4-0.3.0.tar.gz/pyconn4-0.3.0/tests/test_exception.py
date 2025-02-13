import pytest
from pyconn.db.kdb import KDB, Server
from qpython.qreader import QException

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

def test_exception(db):
    q = KDB(server=db)
    sql = "{'wrong}[]"
    with pytest.raises(QException):
        q.query_sync(sql)
