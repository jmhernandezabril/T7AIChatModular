# routes/orchestrator_routes.py

from flask import Blueprint, request, jsonify
import yaml

from orchestrator.schema import PipelineConfig
from orchestrator.runner import load_pipeline

orch_bp = Blueprint("orchestrator", __name__)

@orch_bp.post("/run_chain")
def run_chain():
    """
    Invoca un pipeline declarativo por su nombre y argumentos.
    Body esperado (JSON):
      {
        "pipeline": "nombre_del_yaml_sin_extensión",
        "args": {
          "var1": valor1,
          "var2": valor2,
          ...
        }
      }
    """
    body = request.get_json() or {}
    pipeline_name = body.get("pipeline")
    args = body.get("args", {})

    if not pipeline_name:
        return jsonify({"error": "Debe indicar 'pipeline' en el body."}), 400

    # Carga y valida el YAML con Pydantic
    try:
        with open(f"orchestrator/example_pipelines/{pipeline_name}.yaml", "r") as f:
            conf_dict = yaml.safe_load(f)
        cfg = PipelineConfig.model_validate(conf_dict)
    except FileNotFoundError:
        return jsonify({"error": f"Pipeline '{pipeline_name}' no encontrado."}), 404
    except Exception as e:
        return jsonify({"error": f"Error validando pipeline: {e}"}), 400

    # Ejecuta el pipeline
    try:
        runner = load_pipeline(cfg)
        result = runner(**args)
        return jsonify(result)
    except Exception as e:
        # Captura errores de ejecución
        return jsonify({"error": f"Error ejecutando pipeline: {e}"}), 500

# (Opcional) Endpoint para comprobar el estado o listar pipelines
@orch_bp.get("/list_pipelines")
def list_pipelines():
    """
    Devuelve la lista de nombres de todos los YAML disponibles.
    """
    import os
    base = "orchestrator/example_pipelines"
    files = os.listdir(base)
    names = [f[:-5] for f in files if f.endswith(".yaml")]
    return jsonify({"pipelines": names})