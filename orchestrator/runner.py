# orchestrator/runner.py
import jinja2
from .schema import PipelineConfig
from .loader import instantiate_tool

def load_pipeline(conf: PipelineConfig):
    """
    Dado un PipelineConfig, instancia todas las tools y devuelve
    una función `run(**args)` que ejecuta los steps en orden.
    """
    # 1) Instanciar todas las herramientas declaradas
    tools = {t.name: instantiate_tool(t) for t in conf.tools}

    # 2) Función que ejecuta el pipeline
    def run(**run_args):
        context = dict(run_args)
        for step in conf.steps:
            # 2.1) Renderizar inputs con Jinja2 usando el contexto
            rendered_inputs = {
                k: jinja2.Template(str(v)).render(**context)
                for k, v in step.inputs.items()
            }
            # 2.2) Ejecutar la herramienta
            result = tools[step.tool].run(**rendered_inputs)
            # 2.3) Guardar cada output en el contexto
            if isinstance(result, dict):
                for out in step.outputs:
                    context[out] = result.get(out)
        return context

    return run