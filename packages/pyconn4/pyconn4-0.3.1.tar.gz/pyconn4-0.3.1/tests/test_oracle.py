from pyconn.db.oracle import ORACLE
from pyconn.db.oracle import OracleServerInfo


def test_oracle_conn():
    db = OracleServerInfo()
    db.name = "FDB"
    db.sid = "FDB"
    db.username = "FDB"
    db.password = "FDB"

    q = ORACLE(server=db)
    sql = "select * from dual"
    t = q.query(sql)
    t = q.query_pandas(sql)


def test_query_parameters():
    db = OracleServerInfo()
    db.name = "FDB"
    db.sid = "FDB"
    db.username = "FDB"
    db.password = "FDB"

    q = ORACLE(server=db)

    sql = "select a.sym,a.dt,a.open,a.high,a.low,a.close,a.vol,a.amount from ia_quote a where a.dt=to_date(:dt, 'yyyymmdd') order by a.sym,a.dt"

    t = q.query(sql, {"dt": "20170213"})
    t = q.query_pandas(sql, {"dt": "20170213"})
