import glob
import yaml
import pytest
from orchestrator.schema import PipelineConfig
from orchestrator.runner import load_pipeline

@pytest.mark.parametrize("path", glob.glob("orchestrator/example_pipelines/*.yaml"))
def test_runner_ejecuta_sin_error(path):
    conf_dict = yaml.safe_load(open(path))
    conf = PipelineConfig.model_validate(conf_dict)
    runner = load_pipeline(conf)

    # preparamos args mínimos: para cada variable en inputs usamos un valor genérico
    dummy_args = {}
    for step in conf.steps:
        for v in step.inputs.values():
            if isinstance(v, str):
                # busca {{ var }} o "{var}"
                if "{{" in v and "}}" in v:
                    var = v.split("{{")[1].split("}}")[0].strip()
                    dummy_args[var] = f"test_{var}"
                elif v.startswith("{") and v.endswith("}"):
                    var = v.strip("{}")
                    dummy_args[var] = f"test_{var}"

    # con esos argumentos, no debe lanzar excepción
    out = runner(**dummy_args)
    # verificar que al menos devuelve el contexto de entrada
    for k in dummy_args:
        assert k in out