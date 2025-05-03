# Orquestador Declarativo: Pasos e Integración en T7AIChatModular

Este documento consolida la **guía de implementación** del orquestador de pipelines y la **estructura de archivos** necesarios, indicando qué ya existe y qué es **nueva a crear**.

---

## 1️⃣ Pasos para crear el orquestador

1. **Crear el módulo `orchestrator/`**

   * Añade estos archivos:

     * `schema.py` (Pydantic: `ToolConfig`, `StepConfig`, `PipelineConfig`)
     * `loader.py` (`instantiate_tool`)
     * `runner.py` (`load_pipeline`)
     * Carpeta `example_pipelines/` con `ejemplo_simple.yaml` (pipeline de prueba)

   * **Test**: escribe un test en `tests/test_pipeline_schema.py` que cargue el YAML de ejemplo y valide con Pydantic.

   > 👉 Con esto tendrás tu “máquina de pipelines” local con validación automática.

2. **Integración interna en el chat**

   * Modifica `routes/chat_routes.py` para detectar un comando:

     ```bash
     !run ejemplo_simple name=Foo
     ```

   * Importa el orquestador y ejecuta:

     ```python
     from orchestrator.schema import PipelineConfig
     from orchestrator.runner import load_pipeline
     import yaml
     # ...
     cfg = PipelineConfig.parse_obj(yaml.safe_load(open("orchestrator/example_pipelines/ejemplo_simple.yaml")))
     runner = load_pipeline(cfg)
     output = runner(name="Foo")
     ```

   * Prueba con `flask run` y confirma que recibes la salida del runner.

   > 👉 Valida la lógica end-to-end sin exponer aún HTTP extra.

3. **Exponer el endpoint `/run_chain`**

   * Crea `routes/orchestrator_routes.py` con un blueprint `orch_bp`:

     ```python
     from flask import Blueprint, request, jsonify
     import yaml
     from orchestrator.schema import PipelineConfig
     from orchestrator.runner import load_pipeline

     orch_bp = Blueprint("orchestrator", __name__)

     @orch_bp.post("/run_chain")
     def run_chain():
         body = request.json
         name = body["pipeline"]
         args = body.get("args", {})
         cfg = PipelineConfig.parse_obj(yaml.safe_load(open(f"orchestrator/example_pipelines/{name}.yaml")))
         runner = load_pipeline(cfg)
         return jsonify(runner(**args))
     ```

   * Registra `orch_bp` en `app.py`:

     ```python
     from routes.orchestrator_routes import orch_bp
     app.register_blueprint(orch_bp, url_prefix="/orchestrator")
     ```

   > 👉 Cualquier cliente (chat, UI, scripts) podrá invocar pipelines vía HTTP.

4. **Editor low-code y despliegue**

   * Monta un formulario (Dash o React) que use el **JSON Schema** de `PipelineConfig` para editar/generar YAML y guardarlo en `example_pipelines/`.

   * Añade CI/CD: pruebas de Pydantic, runner y tests de integración chat → pipeline.

   * (Opcional) Conteneriza con Docker, expón con FastAPI o Kubernetes para producción.

   > 👉 Una capa de edición visual y despliegue asegura rapidez y estabilidad.

---

## 🗂️ Estructura de archivos en T7AIChatModular

```
T7AIChatModular/
├── orchestrator/            # NUEVA A CREAR POR ORQUESTACION (Módulo de pipelines declarativos)
│   ├── __init__.py          # NUEVA (Inicializador del paquete)
│   ├── schema.py            # NUEVA (Modelos Pydantic: ToolConfig, StepConfig, PipelineConfig)
│   ├── loader.py            # NUEVA (Lógica para instanciar herramientas dinámicamente)
│   ├── runner.py            # NUEVA (Función load_pipeline y ejecución de steps)
│   └── example_pipelines/   # NUEVA (Carpeta con ejemplos YAML de pipelines)
│       └── ejemplo_simple.yaml  # NUEVA (Pipeline de prueba para validación)
├── services/                # YA EXISTE (Lógica de negocio central)
│   ├── chat_service.py      # YA EXISTE (Orquesta mensaje vs SQL/LLM)
│   └── sql_service.py       # YA EXISTE (Ejecuta y consulta base de datos)
├── routes/                  # YA EXISTE (Definición de rutas HTTP y Dash)
│   ├── chat_routes.py       # YA EXISTE (Endpoints de chat y comando !run interno)
│   ├── orchestrator_routes.py  # NUEVA A CREAR (Blueprint para /run_chain y /run_status)
│   ├── dash_app.py          # YA EXISTE (Inicializa Dash en Flask)
│   ├── dash_callbacks.py    # YA EXISTE (Callbacks para componentes Dash)
│   └── dash_layout.py       # YA EXISTE (Layout y componentes de Dash)
├── tests/                   # YA EXISTE (Pruebas unitarias con pytest)
│   └── test_pipeline_schema.py  # NUEVO A CREAR (Test de validación de YAML con Pydantic)
├── app.py                   # YA EXISTE (Punto de entrada, registra routers y blueprints)
├── config.py                # YA EXISTE (Variables de entorno y configuración global)
├── static/                  # YA EXISTE (Recursos CSS/JS para UI de chat)
├── templates/               # YA EXISTE (Plantillas Jinja2 para chat)
└── vector_memory/           # YA EXISTE (Módulo FAISS y embeddings)
```

Con este único documento tienes:

* La **guía de pasos** para implementar el orquestador.
* La **estructura** de carpetas y archivos indicando qué ya existe y qué crear.

Así podrás llevar a cabo la orquestación declarativa de forma ordenada y coherente.

---
* QUÉ SIGUE AHORA?
  
◻️ !run ejemplo_simple nombre=ChatGPT
* 
◻️ **Construir pipelines reales**  
   - Crea un YAML para tu caso de uso (p.ej. `alta_pedido.yaml`) en `example_pipelines/`.  
   - Prueba con `!run alta_pedido …` para verificar su ejecución.

◻️ **Slot-filling y validaciones**  
   - Detecta errores (p.ej. productos no válidos) e inicia diálogos de corrección.  
   - Emplea sub-pipelines (`pipeline` tool) para búsquedas y dispatch condicional.

◻️ **Mejorar el frontend**  
   - Ajusta `chat.js` para renderizar `data` con tablas, botones de selección y edición inline.  
   - Soporta uploads de Excel y componentes visuales sin salir del chat.

◻️ **Exponer la API**  
   - Añade `routes/orchestrator_routes.py` con endpoint `/run_chain` (y `/run_status`).  
   - Registra el blueprint en `app.py` para invocaciones externas.

◻️ **Tests y CI**  
   - Escribe tests de integración para el comando `!run` y el endpoint `/chat`.  
   - Configura CI (GitHub Actions, flake8, pytest) para asegurar calidad y despliegues.

