# Hitos y Documentación de T7AIChatModular

Este documento recoge los principales **hitos** alcanzados en el desarrollo de T7AIChatModular y explica cómo funcionan las piezas clave de la plataforma.

---

## 1. Ejecución de DDL y DML desde el chat

1. **Comandos soportados**  
   - `CREATE`, `ALTER`, `DROP` (DDL)  
   - `INSERT`, `UPDATE`, `DELETE` (DML)  
   - `SELECT` (Consultas)

2. **Persistencia y documentación**  
   - Al ejecutar un `CREATE` (u otro DDL), se graba una entrada en Markdown que documenta la sentencia.  
     ![IMG1: Documentación automática de DDL](path/to/img1_placeholder)
   - Se apoyan en los módulos:
     - **db_manager.py**: gestiona la conexión a SQLite y la ejecución de SQL.  
     - **doc_manager.py**: genera y actualiza los ficheros Markdown con el histórico de DDL.  
     ![IMG2: Diagrama de módulos DB y DOC Manager](path/to/img2_placeholder)

3. **Flujo de una consulta**  
   - El usuario escribe `SELECT ...` en el chat.  
   - `chat_routes.py` recibe la petición, llama a `query_sql()`.  
   - Los resultados se retornan al chat y se almacenan en `app.last_query_df` para su posterior uso.

---

## 2. Panel interactivo con Dash

1. **Componentes principales**  
   - **dash_app.py**: inicializa la aplicación Dash y configura el layout dinámico.  
   - **dash_layout.py**: define la estructura visual (dropdowns, gráficos, tabla, botones).  
   - **dash_callbacks.py**: implementa la lógica reactiva para actualizar gráficos y tablas.  

2. **Funcionamiento**  
   - Al ejecutar un `SELECT`, los datos se vuelcan en `app.last_query_df`.  
   - Accediendo a `/dash/`, Dash lee ese DataFrame y reconstruye el layout con:
     - Gráfico dinámico (bar, line, scatter, pie).  
     - Tabla de datos con todas las columnas.  
     - Controles para exportar a Excel.  
   ![IMG3: Ejemplo del panel Dash](path/to/img3_placeholder)

3. **Export a Excel**  
   - Ruta Flask `/download_excel` que convierte `last_query_df` en un fichero `.xlsx` y lo sirve al cliente.

---

## Próximos pasos de documentación

- Añadir capturas reales en lugar de placeholders (IMG1, IMG2, IMG3).  
- Describir más en detalle cada endpoint de Flask y cada callback de Dash.  
- Mantener este documento en `/docs/` y actualizarlo tras cada hito o nueva funcionalidad.

---

*Documento generado automáticamente como parte de la fase de documentación de T7AIChatModular.*