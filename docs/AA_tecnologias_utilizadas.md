# 🛠️ Tecnologías Utilizadas en T7AIChatModular

Este proyecto combina diferentes tecnologías modernas para construir un copiloto conversacional modular, flexible y expansible.

---

## 🔹 Backend

| Área                                 | Tecnología              | Fabricante / Comunidad   |
|:-------------------------------------|:------------------------|:-------------------------|
| Framework web ligero                 | Flask                   | Open Source              |
| Procesamiento de lenguaje natural    | LangChain               | LangChain Inc.           |
| Orquestación de flujos IA            | LangGraph               | LangChain Inc.           |
| Agentes IA Avanzados                 | AutoGen                 | Microsoft Research       |
| Resolución de subjetividades         | CAMEL Framework         | Stanford University      |
| Base de datos local                  | SQLite                  | Open Source              |

---

## 🔹 Inteligencia Artificial

| Área                                           | Tecnología                             | Fabricante / Comunidad    |
|:-----------------------------------------------|:---------------------------------------|:--------------------------|
| Motor de IA principal                          | OpenAI (gpt-3.5-turbo)                 | OpenAI                    |
| Memoria semántica con recuperación por similitud | FAISS + Embeddings OpenAI              | Meta AI + OpenAI          |
| Clasificación avanzada de intenciones (opcional) | HuggingFace Transformers               | HuggingFace Community     |

**🔍 FAISS (Facebook AI Similarity Search)** permite a T7AIChatModular buscar información relevante en tiempo real basándose en el contenido conversacional previo o documentos embebidos.  
El sistema ya incorpora un índice vectorial activo que se puede alimentar, consultar y actualizar dinámicamente desde el módulo `vector_memory/`.

---

## 🔹 Frontend

| Área                                | Tecnología                                           | Fabricante / Comunidad       |
|:------------------------------------|:-----------------------------------------------------|:-----------------------------|
| Plantillas HTML dinámicas           | Jinja2 (integrado en Flask)                          | Pallets Projects             |
| Visualización de gráficos rápidos   | Plotly                                              | Plotly Inc.                  |
| Visualización avanzada de paneles   | Plotly Dash (dash + dash-bootstrap-components)      | Plotly Inc. / Faculty AI     |
| Estilos web                         | CSS propio (con posible Tailwind futuro)             | Open Source                  |

> **Anteriormente se consideró Streamlit**, pero por la necesidad de mayor flexibilidad, modularidad y potencia reactiva, se optó por **Dash** como solución definitiva.

---

## 🔹 Machine Learning y Deep Learning

| Área                        | Tecnología            | Fabricante / Comunidad |
|:----------------------------|:----------------------|:-----------------------|
| Pipelines clásicos          | Scikit-learn          | Open Source            |
| Series temporales           | Prophet / ARIMA       | Facebook / Statsmodels |
| Deep Learning               | TensorFlow, PyTorch   | Open Source            |
| Model serving               | Flask / FastAPI       | Open Source            |

**Flujo de ejemplo**:
1. **Entrenamiento offline** en Jupyter: carga datos de `visitas` con Pandas, entrena un `RandomForestRegressor` o un LSTM, y guarda el modelo (Pickle, SavedModel, ONNX).  
2. **Servicio de inferencia** con un endpoint `/predict`: Flask o FastAPI carga el modelo y responde predicciones.  
3. **Integración en Chat y Dash**: comandos como `PREDICT_visitas` en el chat o un botón `Predecir` en Dash que consume `/predict` y muestra resultados gráficos.

---

## 🔹 Orquestación Declarativa de Flujos IA

En lugar de codificar cada pipeline en Python, se puede usar **configuración declarativa (YAML/JSON)** para definir agentes, chains y herramientas:

- **YAML/JSON**: describe agentes, herramientas (`tools`), pipelines (`chains`) y pasos.  
- **Pydantic / JSON Schema**: valida la configuración antes de instanciar.  
- **Orchestrator dinámico**: módulo que lee la config y crea instancias de `LLMChain`, `Agents`, `Tools` y `Memories` usando `importlib`.  
- **Dispatcher API**: endpoint (`/run_chain`) que recibe el nombre del flujo y el input, ejecuta el chain y devuelve resultados JSON.  
- **UI low-code**: usar Dash o react-jsonschema-form para editar pipelines en la web con validación.  
- **GitOps y hot-reload**: versiona la config en Git, y recarga cambios al vuelo con file‐watcher (watchdog) sin reiniciar servicios.

**Beneficios**: modularidad sin escribir código, despliegue de nuevos flujos solo editando ficheros, validación automática y editor gráfico.

---

## 🔹 Documentación y Organización

| Área                        | Tecnología / Formato         |
|:----------------------------|:-----------------------------|
| Documentación técnica       | Markdown (`.md`)             |
| Organización modular        | Carpeta `/docs/`             |
| Control de configuraciones  | `config.py` centralizado     |
| Seguimiento de pushes       | `logs/git_push.log` automático |

---

# 🎯 Visión Final

T7AIChatModular combina inteligencia artificial, memoria vectorial, orquestación modular de flujos, visualización interactiva y análisis predictivo con pipelines ML/DL y orquestación declarativa, para construir un asistente conversacional vivo, adaptable y preparado para evolucionar sin tocar código, solo configuraciones.  
