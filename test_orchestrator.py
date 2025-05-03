import yaml
from orchestrator.schema import PipelineConfig
from orchestrator.runner import load_pipeline

# 1) Carga y valida con model_validate en lugar de parse_obj
conf = PipelineConfig.model_validate(
    yaml.safe_load(open("orchestrator/example_pipelines/ejemplo_simple.yaml"))
)

# 2) Crea el runner y ejecuta
runner = load_pipeline(conf)
out = runner(nombre="ChatGPT")

# 3) Muestra el resultado
print(out)