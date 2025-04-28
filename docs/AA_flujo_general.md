# 🔄 Flujo General de Procesamiento

Este documento describe el flujo completo del copiloto `T7AIChatModular`, desde que el usuario envía un mensaje hasta que se muestra una respuesta, integrando componentes clave como FAISS, CAMEL Framework y Transformers.

---

## 1️⃣ Entrada del Usuario

```plaintext
[Usuario escribe]
```
- Entrada por interfaz web (Flask) o paneles interactivos (Streamlit).
- Se captura el mensaje y se inicia o recupera la sesión.

---

## 2️⃣ Recepción por el Backend

```plaintext
[Flask app.py recibe mensaje]
```
- `app.py` es el punto de entrada del backend.
- Pasa el mensaje al ruteador de intenciones.

---

## 3️⃣ Clasificación de Intención

```plaintext
[LangChain Router clasifica intención]
```
- Utiliza `intent_classifier.py` para detectar la intención (alta, consulta, etc.).
- **CAMEL Framework** puede intervenir si hay subjetividad o ambigüedad.
- Se puede usar clasificación avanzada mediante **HuggingFace Transformers**.

---

## 4️⃣ Orquestación del Flujo

```plaintext
[LangGraph Flows gestiona flujo]
```
- Cada intención activa un flujo específico (grafo de nodos).
- Cada nodo puede ser una herramienta, un agente o una acción.

---

## 5️⃣ Memoria Semántica con FAISS

```plaintext
[Consulta FAISS (si aplica)]
```
- Si la intención requiere contexto documental:
  - `vector_memory/faiss_manager.py`
  - `vector_memory/embedder.py`
  - `vector_memory/loader.py`
- Se obtienen resultados relevantes mediante búsqueda vectorial.

---

## 6️⃣ Generación de Respuesta IA

```plaintext
[Respuesta IA generada]
```
- Se genera usando `llm_manager.py` (por defecto: GPT-3.5-Turbo).
- Puede combinarse con resultados de FAISS y CAMEL.

---

## 7️⃣ Visualización y Renderizado

```plaintext
[Renderizado en index.html]
```
- Web tradicional: HTML (Jinja2)
- Visualizaciones: Streamlit en `/paneles/`

---

# 🔗 Flujo Inteligente de Gestor de Base de Datos

T7AIChatModular también gestiona la evolución de la estructura de la base de datos a través de lenguaje natural, de forma segura y controlada.

## 1️⃣ Interpretación de Peticiones

- Analiza si la petición implica:
  - Crear una tabla
  - Modificar estructura (añadir/modificar columnas)
  - Eliminar estructura (solo administradores)

## 2️⃣ Generación de SQL Seguro

- Genera el comando SQL correspondiente:
  - Usuarios normales: solo estructura (CREATE, ALTER)
  - Administradores: permitido también DELETE, DROP, INSERT, UPDATE (con doble confirmación)

## 3️⃣ Confirmación de Seguridad

- Usuarios normales: 1 confirmación.
- Administradores (`administrador_bd`): 2 confirmaciones para operaciones destructivas.

## 4️⃣ Ejecución y Actualización

- Ejecuta el comando en la base de datos.
- Actualiza el documento `AZ_base_datos.md` con las nuevas tablas o campos.
- Actualiza el índice FAISS para reflejar la nueva estructura en las búsquedas IA.

## 5️⃣ Registro de Cambios

- Toda operación queda registrada en el sistema de logs para auditoría y trazabilidad.

---

# 🔗 Resumen de Componentes IA en el Flujo

| Tecnología | Rol en el Flujo | Comunidad |
|------------|------------------|-----------|
| CAMEL Framework | Resolución de subjetividades | Stanford University |
| FAISS | Memoria semántica vectorial | Meta AI |
| HuggingFace Transformers | Clasificación avanzada de intenciones | HuggingFace |
| LangChain Router | Dirección por intención | LangChain Inc. |
| LangGraph | Orquestación de flujos IA | LangChain Inc. |
| GPT-3.5-Turbo | Motor LLM de generación | OpenAI |

---

Este flujo modular permite escalar, personalizar e incorporar nuevas funciones en cualquier fase, incluyendo la evolución automática de la base de datos de manera segura.