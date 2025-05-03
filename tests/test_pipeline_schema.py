import glob
import yaml
import pytest
from orchestrator.schema import PipelineConfig

@pytest.mark.parametrize("path", glob.glob("orchestrator/example_pipelines/*.yaml"))
def test_pipeline_schema_valido(path):
    conf_dict = yaml.safe_load(open(path))
    # valida que Pydantic lo acepta
    conf = PipelineConfig.model_validate(conf_dict)
    assert conf.name  # al menos debe tener un nombre
    assert isinstance(conf.tools, list)
    assert isinstance(conf.steps, list)