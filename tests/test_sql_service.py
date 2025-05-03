# tests/test_sql_service.py

import pytest
from services.sql_service import SQLService

# Fakes to override the real executors in modules/sql_executor
def fake_manual(sql, usuario):
    return {"success": f"OK DDL/DML: {sql}"}

def fake_select(sql):
    return {
        "response": [["r1", "r2"]],
        "columns": ["c1", "c2"],
        "dataframe": [[1, 2], [3, 4]]
    }

@pytest.fixture(autouse=True)
def patch_sql(monkeypatch):
    import modules.sql_executor as mod
    monkeypatch.setattr(mod, "ejecutar_sql_manual", fake_manual)
    monkeypatch.setattr(mod, "ejecutar_consulta_select", fake_select)

def test_ddl_goes_to_manual():
    svc = SQLService(ddl_cmds=["CREATE"], dml_cmds=[])
    out = svc.handle("CREATE TABLE X(id INT)", "user1")
    assert out == {"response": "OK DDL/DML: CREATE TABLE X(id INT)"}

def test_select_goes_to_select():
    svc = SQLService(ddl_cmds=[], dml_cmds=[])
    out = svc.handle("SELECT * FROM tabla", "user1")
    assert out["response"] == [["r1", "r2"]]
    assert out["columns"] == ["c1", "c2"]
    assert out["dataframe"] == [[1, 2], [3, 4]]

def test_non_sql_returns_none():
    svc = SQLService(ddl_cmds=[], dml_cmds=[])
    assert svc.handle("Hola Mundo", "user1") is None