# 🛠️ Tecnologías Utilizadas en T7AIChatModular

Este proyecto combina diferentes tecnologías modernas para construir un copiloto conversacional modular, flexible y expansible.

---

## 🔹 Backend

| Área | Tecnología | Fabricante / Comunidad |
|:-----|:------------|:-----------------------|
| Framework web ligero | Flask | Open Source |
| Procesamiento de lenguaje natural | LangChain | LangChain Inc. |
| Orquestación de flujos IA | LangGraph | LangChain Inc. |
| Agentes IA Avanzados | AutoGen | Microsoft Research |
| Resolución de subjetividades | CAMEL Framework | Stanford University |
| Base de datos local | SQLite | Open Source |

---

## 🔹 Inteligencia Artificial

| Área | Tecnología | Fabricante / Comunidad |
|:-----|:-----------|:------------------------|
| Motor de IA principal | OpenAI (gpt-3.5-turbo) | OpenAI |
| Memoria semántica con recuperación por similitud | FAISS + Embeddings OpenAI | Meta AI + OpenAI |
| Clasificación avanzada de intenciones (opcional) | HuggingFace Transformers | HuggingFace Community |

**🔍 FAISS (Facebook AI Similarity Search)** permite a T7AIChatModular buscar información relevante en tiempo real basándose en el contenido conversacional previo o documentos embebidos.  
El sistema ya incorpora un índice vectorial activo que se puede alimentar, consultar y actualizar dinámicamente desde el módulo `vector_memory/`.

---

## 🔹 Frontend

| Área | Tecnología | Fabricante / Comunidad |
|:-----|:-----------|:------------------------|
| Plantillas HTML dinámicas | Jinja2 (integrado en Flask) | Pallets Projects |
| Visualización de gráficos rápidos | Plotly | Plotly Inc. |
| Visualización avanzada de paneles | Streamlit | Streamlit (Snowflake) |
| Estilos web | CSS propio (con posible Tailwind futuro) | Open Source |

---

## 🔹 Documentación y Organización

| Área | Tecnología / Formato |
|:-----|:----------------------|
| Documentación técnica | Markdown (`.md`) |
| Organización modular | Carpeta `/docs/` |
| Control de configuraciones | `config.py` centralizado |
| Seguimiento de pushes | `logs/git_push.log` automático |

---

# 🎯 Visión Final

T7AIChatModular combina inteligencia artificial, memoria vectorial, orquestación modular de flujos y visualización interactiva para construir un asistente conversacional vivo, adaptable y preparado para evolucionar.

---
