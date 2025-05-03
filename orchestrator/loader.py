# orchestrator/loader.py
from .schema import ToolConfig

def instantiate_tool(cfg: ToolConfig):
    """
    Dada una configuración de herramienta, devuelve una instancia
    de la clase correspondiente.
    """
    # Ejemplo para SQL
    if cfg.type == "sql_query":
        from orchestrator.tools.sql_tool import SQLTool
        return SQLTool(**cfg.params)

    # Ejemplo para LLMChain
    if cfg.type == "llm_chain":
        from orchestrator.tools.llm_chain_tool import LLMChainTool
        return LLMChainTool(**cfg.params)

    # Ejemplo para CAMEL Agent
    if cfg.type == "camel_agent":
        from orchestrator.tools.camel_agent_tool import CAMELAgentTool
        # Instancia sub-herramientas si las hay
        subtools = [
            instantiate_tool(ToolConfig.parse_obj(t))
            for t in cfg.params.get("tools", [])
        ]
        # Quita la clave 'tools' de params antes de pasar al constructor
        base_params = {k: v for k, v in cfg.params.items() if k != "tools"}
        return CAMELAgentTool(tools=subtools, **base_params)

    raise ValueError(f"Tipo de herramienta desconocido: {cfg.type}")