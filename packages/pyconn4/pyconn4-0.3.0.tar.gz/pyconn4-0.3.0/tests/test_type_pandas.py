import numpy as np
import pandas as pd
import pytest
from qpython import qcollection
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


def test_type_native(db):
    db.pandas = False
    q = KDB(db)
    assert isinstance(q.query_sync("{x}", np.bytes_("你好", encoding="utf-8")), bytes)
    assert isinstance(q.query_sync("til 10"), qcollection.QList)
    assert isinstance(q.query_sync("flip `a`b!(10?.Q.n;10?.Q.a)"), qcollection.QTable)


def test_type_pandas(db):
    db.pandas = True
    q = KDB(db)
    s = q.query_sync("til 10")
    assert isinstance(s, pd.core.series.Series)
    assert s.shape == (10,)
    df = q.query_sync("flip `a`b!(10?.Q.n;10?.Q.a)")
    assert isinstance(df, pd.core.frame.DataFrame)
    assert df.shape == (10, 2)
