# 🏗️ Estructura Técnica de T7AIChatModular

## Módulos principales

```plaintext
/project-root/
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── /modules/
│   ├── intent_classifier.py
│   ├── langchain_router.py
│   ├── langgraph_flows.py
│   ├── llm_manager.py
│   └── session_manager.py
│
├── /vector_memory/
│   ├── faiss_manager.py         # Gestión de índice FAISS
│   ├── embedder.py              # Generación de embeddings
│   └── loader.py                # Carga de documentos al índice
│
├── /templates/
│   └── index.html
│
├── /static/
│   └── css/
│       └── style.css
│
├── /paneles/
│   └── panel_streamlit.py
│
└── /docs/
    ├── README.md
    ├── modelo_IA.md
    ├── tecnologias_utilizadas.md
    └── guia_push_git_token.md
