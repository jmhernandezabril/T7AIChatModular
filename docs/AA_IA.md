# 🧠 Motor IA Utilizado (por defecto, podrá ser otro)

- **Proveedor**: OpenAI  
- **Modelo**: GPT-3.5 Turbo (`gpt-3.5-turbo`)  
- **Temperatura**: 0.3  
- **Tokens máximos**: 1000

**Uso actual**:
- Clasificación de intenciones y entidades.  
- Generación de respuestas IA.  
- Ayuda dinámica conversacional.

---

## 📦 Resumen de la arquitectura IA del proyecto

Este proyecto integra una cadena completa de tecnologías IA para ofrecer una plataforma conversacional y de análisis:

1. **ChatOps & SQL interactivo**:
   - Comandos DDL/DML (`CREATE`, `ALTER`, `INSERT`, `SELECT`, etc.) desde el chat.
   - Ejecución en SQLite y documentación automática de cambios en Markdown.

2. **Orquestación de flujos conversacionales**:
   - **LangChain Graph** dirige pipelines y sub-agentes (CAMEL) para operaciones CRUD, analytics y reporting.

3. **Memoria semántica global y por usuario**:
   - **FAISS** indexa conversaciones y metadatos.
   - Se segmenta por `user_id` (por defecto `t7AI`), permitiendo recuperar el historial y preferencias de cada usuario.
   - **ConversationBufferMemory** de LangChain guarda el contexto individual de cada sesión.

4. **Visualización reactiva**:
   - **Dash** genera dashboards con gráficos dinámicos, tablas filtrables, drill-downs y export a Excel.

5. **Machine Learning & Deep Learning**:
   - **Scikit-learn** para pipelines clásicos de regresión, clasificación y clustering.
   - **Prophet / ARIMA** para forecasting de series temporales.
   - **TensorFlow / PyTorch** para redes neuronales profundas (LSTM, Transformers, CNN).
   - Model serving con Flask/FastAPI para endpoints de inferencia en tiempo real (`/predict`).

---

## 🔑 Memoria de usuario personalizada

Para adaptar el sistema al perfil de cada usuario:

- **Identificación**: `@app.before_request` en Flask fija `g.user_id` (fallback `t7AI`).
- **Per-user FAISS index**: cada usuario tiene su propio índice o metadatos en el índice global.
- **Recuperación filtrada**: los retrievers de LangChain devuelven solo documentos asociados a ese `user_id`.
- **Contexto conversacional**: `ConversationBufferMemory` almacena la sesión específica como parte de los callbacks.
- **Feedback loop**: se indexan las interacciones aceptadas o rechazadas para mejorar la personalización.

**Beneficios**:
- Respuestas y recomendaciones contextualizadas.  
- Búsquedas semánticas que reflejan preferencias y historial.  
- Evolución continua del modelo con cada interacción.

---

> *Con esta arquitectura 100% Python-First, T7AIChatModular se convierte en un sistema de “Data‑Ops Conversacional” modular, adaptativo y escalable, capaz de gestionar esquemas, datos, visualizaciones y modelos predictivos desde un único chat.*

