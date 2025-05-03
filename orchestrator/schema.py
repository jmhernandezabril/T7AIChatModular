# orchestrator/schema.py
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class ToolConfig(BaseModel):
    name: str
    type: str                      # p.ej. "sql_query", "llm_chain", "camel_agent"
    params: Dict[str, Any] = Field(default_factory=dict)

class StepConfig(BaseModel):
    name: str
    tool: str                      # referencia al nombre de la herramienta
    inputs: Dict[str, Any] = Field(default_factory=dict)
    outputs: List[str] = Field(default_factory=list)
    when: Optional[str] = None     # condición opcional (evaluada como Jinja2)
    retries: Optional[int] = 1     # número de reintentos en caso de fallo

class PipelineConfig(BaseModel):
    name: str
    description: Optional[str] = None
    tools: List[ToolConfig]
    steps: List[StepConfig]
