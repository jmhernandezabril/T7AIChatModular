# orchestrator/tools/llm_chain_tool.py
from jinja2 import Template

class LLMChainTool:
    def __init__(self, prompt_template: str, **kwargs):
        # Guardamos el template Jinja2
        self.template = Template(prompt_template)

    def run(self, **inputs):
        """
        Renderiza el prompt con los inputs y lo devuelve como 'response'.
        Así simulamos un LLM que simplemente rellena el template.
        """
        rendered = self.template.render(**inputs)
        return {"response": rendered}