# Documentación de la Estructura Modular de **T7AIChatModular**

Este documento describe la organización del proyecto **T7AIChatModular** siguiendo principios de modularización y escalabilidad.

---

## 1. Visión General

* **Objetivo**: Proveer un chatbot híbrido que combina procesamiento de lenguaje natural (LLM) con ejecución de sentencias SQL, además de un panel Dash para visualización de resultados.
* **Tecnologías principales**: Flask, LangChain/OpenAI, SQLite, Dash, FAISS (vector\_memory).

---

## 2. Entry Points

* `app.py` / `main.py`: inicializan y configuran la aplicación Flask. Definen:

  * Registro de rutas (`routes/chat_routes.py`, `routes/dash_app.py`).
  * Inicialización de la instancia Dash (submódulo `/routes/dash_*.py`).
  * Carga de configuración desde `config.py`.

---

## 3. Configuración Global

* `config.py`: parámetros de entorno y constantes:

  * Rutas y motor de base de datos (`DB_PATH`, `DB_ENGINE`).
  * Credenciales/API keys (`OPENAI_API_KEY`, `AI_MODEL`, etc.).
  * Comandos SQL permitidos (`DDL_COMMANDS`, `DML_COMMANDS`).
  * Parámetros UI (estilos, mensajes iniciales).
* `.env` / `.replit`: variables de entorno y configuración del entorno de ejecución.

---

## 4. Servicios de Lógica de Negocio

### 4.1 `services/chat_service.py`

* Encapsula la lógica de atención de mensajes:

  1. Distingue entre comandos DDL, DML y small-talk.
  2. Orquesta llamadas a `sql_service` y al LLM (`langchain`).
  3. Devuelve una respuesta unificada con estructura: `{{ response, rows?, columns? }}`.

### 4.2 `services/sql_service.py`

* Maneja la ejecución de sentencias SQL:

  * Implementa abstracciones: `execute_sql()`, `query_sql()`.
  * Documenta acciones (`doc_manager.documentar_sql`).
  * Permite extenders para otros motores (PostgreSQL, MySQL) adaptando `connect_db()`.

---

## 5. Capa de Persistencia de Vectores

* `vector_memory/`:

  * `config_vector.py`: parámetros de embeddings.
  * `embeddings.py`: wrapper de OpenAI Embeddings.
  * `index_faiss.py`: configuración y gestión de índice FAISS.
* **Responsabilidad**: aislar la lógica de memoria semántica, permitiendo cambiar de FAISS a otro motor (ANN) sin impactar otros módulos.

---

## 6. Rutas HTTP y Panel de Control

### 6.1 `routes/chat_routes.py`

* Endpoint `/chat`: recibe mensajes JSON, llama a `ChatService.handle_message()`, y:

  * Si hay `rows`/`columns`, construye un `DataFrame` para Dash y retorna JSON.
  * Si es DDL/DML o small-talk, devuelve solo texto.
* Endpoint `/` (base): renderiza `templates/base.html`.

### 6.2 `routes/dash_app.py`, `routes/dash_callbacks.py`, `routes/dash_layout.py`

* Configuran la aplicación Dash montada en Flask:

  * `dash_layout.py`: definición de componentes gráficos y contenedores.
  * `dash_callbacks.py`: funciones reactivas para actualizar gráficos según `app.last_query_df`.
  * `dash_app.py`: fábrica de la instancia Dash, registro de layout y callbacks.

---

## 7. Componentes Front-End

* `static/css/base.css`: estilos globales.
* `static/js/chat.js`: manejo de la UI de chat (envío de mensajes, renderizado de respuestas).
* `templates/base.html`: plantilla principal que incluye chat y link al panel avanzado.

---

## 8. Pruebas Unitarias

* `tests/`:

  * `test_chat_service.py`: cubre flujos de `ChatService` (small-talk, SQL vs LLM).
  * `test_sql_service.py`: verifica `execute_sql()`, `query_sql()` y helpers (`create_table_if_not_exists`).
  * `test_routes.py`: pruebas de las rutas `/chat` y endpoints relacionados (status codes, payloads JSON).

---

## 9. Puntos de Escalabilidad y Extensión

1. **Módulo de Bases de Datos** (`services/sql_service.py`)

   * Fácil de adaptar a otros motores (añadir `psycopg2`, `mysqlclient`).
   * Separación clara de `execute` vs `query` vs documentación.

2. **Servicio Chat** (`services/chat_service.py`)

   * Arquitectura plug-and-play: cambiar LLM (OpenAI → Azure → Anthropic) modificando solo la instancia del modelo.
   * Posibilidad de añadir más *intents* (p. ej. reportes, análisis de datos) orquestando nuevos módulos.

3. **Memoria Vectorial** (`vector_memory/`)

   * Aislamiento total: cambiar FAISS por Annoy, HNSW, etc., sin tocar servicios ni rutas.

4. **Panel Dash**

   * Usa estado compartido (`app.last_query_df`) para desacoplar servicio de chat y visualización.
   * Separación UI (layout, callbacks) que facilita introducir nuevos gráficos/componentes.

5. **Pruebas**

   * Cobertura unitaria coherente por módulo, permitiendo refactorizaciones seguras.

---

> **Conclusión**: La estructura actual de **T7AIChatModular** promueve la separación de responsabilidades, facilita pruebas unitarias y permite la ampliación a nuevos motores de base de datos, proveedores de IA y componentes de UI sin acoplamientos rígidos.

---

## Árbol de directorios principal

A continuación se muestra la estructura de carpetas y archivos en la raíz del proyecto, con un breve comentario de cada elemento:

```
T7AIChatModular/
├── .breakpoints            # Configuración de puntos de ruptura del IDE (seguro de eliminar)
├── .env                    # Variables de entorno
├── .gitignore              # Archivos y carpetas ignorados por Git
├── .replit                 # Configuración de Replit (opcional)
├── COMMIT_EDITMSG          # Artefacto de Git (puede eliminarse)
├── HEAD                    # Artefacto de Git (puede eliminarse)
├── README.md               # Documentación del proyecto
├── app.py                  # Punto de entrada principal de Flask
├── config.py               # Configuración global (API keys, rutas, comandos SQL)
├── git_push.sh             # Script de despliegue (opcional)
├── index                   # Archivo no utilizado (revisar/elimnar)
├── main.py                 # Alternativa de punto de entrada (revisar redundancia)
├── modules/                # Módulos de lógica interna (DB, LLM, utilidades)
│   ├── db_manager.py       # Abstracción de ejecución de SQL y documentación
│   ├── llm_manager.py      # Orquestación de llamadas al LLM y ejecución SQL
│   └── __init__.py         # Inicializador de paquete
├── routes/                 # Definición de rutas Flask y panel Dash
│   ├── chat_routes.py      # Endpoints de chat y gestión de SELECT para Dash
│   ├── dash_app.py         # Configuración de la instancia Dash en Flask
│   ├── dash_callbacks.py   # Callbacks Reactivos para componentes Dash
│   └── dash_layout.py      # Layout y componentes de la interfaz Dash
├── services/               # Lógica de negocio principal
│   ├── chat_service.py     # Servicio que gestiona mensajes LLM vs SQL
│   └── sql_service.py      # Helpers de ejecución y consulta SQL
├── static/                 # Recursos estáticos (CSS, JS)
│   ├── css/
│   │   └── base.css         # Estilos globales
│   └── js/
│       └── chat.js          # Lógica de la UI de chat
├── templates/              # Plantillas Jinja2 para Flask
│   └── base.html            # Plantilla principal con chat y enlace a Dash
├── tests/                  # Pruebas unitarias (pytest)
│   ├── __init__.py
│   ├── test_chat_service.py
│   ├── test_sql_service.py
│   └── test_routes.py
└── vector_memory/          # Módulo de memoria vectorial (FAISS)
    ├── config_vector.py    # Configuración de embeddings
    ├── embeddings.py       # Wrapper de OpenAI Embeddings
    ├── index_faiss.py      # Gestión del índice FAISS
    └── __init__.py         # Inicializador de paquete
```

Con este árbol y descripción, tienes una visión clara de cada componente y su responsabilidad.
