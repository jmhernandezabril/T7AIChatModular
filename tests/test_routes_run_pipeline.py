import glob
import pytest
import yaml
from app import create_app

@pytest.fixture(scope="module")
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

@pytest.mark.parametrize("path", glob.glob("orchestrator/example_pipelines/*.yaml"))
def test_endpoint_run_pipeline(client, path):
    # extraer solo el nombre base del YAML
    pipeline = path.split("/")[-1].rsplit(".", 1)[0]
    # construye un payload con el mínimo: usa parámetro dummy para la primera variable
    conf = yaml.safe_load(open(path))
    # asumimos que el primer input de primer step da la variable
    first_input = list(conf["steps"][0]["inputs"].values())[0]
    if "{{" in first_input:
        var = first_input.split("{{")[1].split("}}")[0].strip()
    elif first_input.startswith("{") and first_input.endswith("}"):
        var = first_input.strip("{}")
    else:
        pytest.skip("Pipeline no tiene inputs renderizables")

    payload = {"message": f"!run {pipeline} {var}=pytestval"}
    resp = client.post("/chat", json=payload)
    data = resp.get_json()

    assert resp.status_code == 200
    # Debe devolver algún texto en response
    assert isinstance(data.get("response"), str)
    # Y el contexto data debe incluir nuestra clave
    assert data["data"].get(var) == "pytestval"