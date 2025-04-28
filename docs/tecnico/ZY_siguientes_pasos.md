# 📅 Roadmap de Desarrollo T7AIChatModular

Este documento recoge los **siguientes pasos** y sus prioridades para avanzar en el proyecto.

---

## 1. Consolidar NL→SQL Chain

**Objetivo**: Permitir al usuario dictar en lenguaje natural comandos DDL/DML y SELECT complejos sin escribir SQL.

- Diseñar y probar prompts que conviertan instrucciones en JSON de esquema (DDL) y en SQL SELECT/JOIN.
- Implementar el _chain_ en LangChain o CAMEL con pasos: `prompt → JSON → parser → execute_sql/query_sql`.
- Validar con ejemplos reales: crear tablas, relaciones y consultas en NL, comprobar el SQL generado.

**Impacto**: 🚀 Alta velocidad de uso y reducción de errores.

---

## 2. Autenticación y Perfilado de Usuarios

**Objetivo**: Introducir login, gestionar preferencias y personalizar la experiencia por usuario.

- Implementar login básico con Flask-Login (email + contraseña).
- Extender la tabla `Usuarios` con campos de perfil (zona, tipo favorito, etc.).
- Inyectar perfil en los prompts iniciales para personalizar respuestas.
- Configurar índice FAISS por `user_id` (fallback `t7AI`).

**Impacto**: 👤 Contexto y recomendaciones adaptadas a cada usuario.

---

## 3. Modularizar Orquestación Declarativa

**Objetivo**: Definir y desplegar flujos IA sin tocar código Python.

- Definir esquema Pydantic para la configuración YAML/JSON de pipelines.
- Construir el loader/parser que instancie LLMChain, Agents y Tools dinámicamente.
- Exponer un endpoint `/run_chain` para invocar pipelines por nombre.
- Desarrollar un editor low-code (Dash o react-jsonschema-form) para editar pipelines.

**Impacto**: ⚙️ Alta flexibilidad, nuevos flujos sin redeploy.

---

## 4. Mejoras UX en Dash

**Objetivo**: Elevar la experiencia visual y de interacción en el dashboard.

- Aplicar un tema Bootstrap y añadir un sidebar para navegación.
- Implementar drill-down y cross-filtering en gráficos.
- Integrar Dash AG-Grid para tablas avanzadas (sorting, edición in-cell, búsquedas).
- Añadir previews (sparklines, mini-tablas) integradas en el chat.

**Impacto**: 🎨 Interfaz más profesional y eficiente.

---

## 5. ML/DL en Producción

**Objetivo**: Pasar de reporting reactivo a análisis predictivo.

- Establecer pipelines offline (notebooks) para entrenamiento de modelos.
- Servir modelos con FastAPI + Uvicorn/Gunicorn en endpoints de inferencia.
- Añadir componentes en Dash para visualizar predicciones frente a datos reales.
- Configurar reentrenamiento programado (Celery o cron) y versionado de modelos (MLflow/DVC).

**Impacto**: 🔮 Valor predictivo y proactivo.

---

## 6. Calidad, Pruebas y Despliegue (CI/CD)

**Objetivo**: Garantizar estabilidad y delivery continuo.

- Escribir tests unitarios para `db_manager`, `chat_routes`, pipelines NL→SQL y callbacks de Dash.
- Desarrollar tests de integración: mocks de LLM, FAISS y endpoints ML.
- Configurar CI/CD con GitHub Actions o GitLab CI que ejecute tests, linters (flake8, black) y construya contenedores Docker.
- Desplegar a staging (Docker + Kubernetes o Dash Enterprise) y monitorizar con Prometheus/Grafana o Sentry.

**Impacto**: 🛠️ Robusteza, mantenimiento ágil y despliegues seguros.

---

## 🚦 Resumen de Prioridades

| Paso                            | Complejidad | Valor rápido  |
|---------------------------------|-------------|---------------|
| NL→SQL chain                    | Medio       | Alto          |
| Auth & perfilado                | Bajo        | Alto          |
| Orquestación declarativa        | Alto        | Medio-Alto    |
| UX Dash (Bootstrap, AG-Grid)    | Medio       | Medio         |
| ML en producción                | Alto        | Alto          |
| Calidad, CI/CD y despliegue     | Medio-Alto  | Crítico       |

---

> **Prioridad de inicio**: NL→SQL chain y Auth & perfilado, como cimientos de la UX diferenciadora.

