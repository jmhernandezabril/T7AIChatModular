```yaml
table: usuarios
date: 2025-04-27
time: 11:29
user: t7AI
action: CREATE
sql: |
  CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                nombre TEXT NOT NULL,
                                                            email TEXT NOT NULL,
                                                                       fecha_alta DATE DEFAULT (DATE('now')), rol TEXT DEFAULT 'usuario', tokens_usados INTEGER DEFAULT 0, tokens_limite INTEGER DEFAULT 100000, modelo_ia TEXT DEFAULT 'gpt-3.5-turbo', proveedor_ia TEXT DEFAULT 'OpenAI', activo INTEGER DEFAULT 1);
```

```yaml
table: usuarios
date: 2025-04-27
time: 11:29
user: t7AI
action: DROP
sql: |
  DROP TABLE usuarios;
```

```yaml
table: usuarios
date: 2025-04-27
time: 11:29
user: t7AI
action: CREATE
sql: |
  CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                nombre TEXT NOT NULL,
                                                            email TEXT NOT NULL,
                                                                       fecha_alta DATE DEFAULT (DATE('now')), rol TEXT DEFAULT 'usuario', tokens_usados INTEGER DEFAULT 0, tokens_limite INTEGER DEFAULT 100000, modelo_ia TEXT DEFAULT 'gpt-3.5-turbo', proveedor_ia TEXT DEFAULT 'OpenAI', activo INTEGER DEFAULT 1);
```

```yaml
table: usuarios
date: 2025-04-27
time: 11:41
user: t7AI
action: DROP
sql: |
  DROP TABLE usuarios;
```

```yaml
table: usuarios
date: 2025-04-27
time: 11:42
user: t7AI
action: CREATE
sql: |
  CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_alta DATE DEFAULT (DATE('now')),
    rol TEXT DEFAULT 'usuario',
    tokens_usados INTEGER DEFAULT 0,
    tokens_limite INTEGER DEFAULT 100000,
    modelo_ia TEXT DEFAULT 'gpt-3.5-turbo',
    proveedor_ia TEXT DEFAULT 'OpenAI',
    activo INTEGER DEFAULT 1
  );
```

```yaml
table: usuarios
date: 2025-04-27
time: 12:08
user: t7AI
action: DROP
sql: |
  DROP TABLE usuarios;
```

```yaml
table: usuarios
date: 2025-04-27
time: 12:09
user: t7AI
action: CREATE
sql: |
  CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_alta DATE DEFAULT (DATE('now')),
    rol TEXT DEFAULT 'usuario',
    tokens_usados INTEGER DEFAULT 0,
    tokens_limite INTEGER DEFAULT 100000,
    modelo_ia TEXT DEFAULT 'gpt-3.5-turbo',
    proveedor_ia TEXT DEFAULT 'OpenAI',
    activo INTEGER DEFAULT 1
  );
```

```yaml
table: usuarios
date: 2025-04-27
time: 12:15
user: t7AI
action: DROP
sql: |
  DROP TABLE usuarios;
```

```yaml
table: usuarios
date: 2025-04-27
time: 12:15
user: t7AI
action: CREATE
sql: |
  CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_alta DATE DEFAULT (DATE('now')),
    rol TEXT DEFAULT 'usuario',
    tokens_usados INTEGER DEFAULT 0,
    tokens_limite INTEGER DEFAULT 100000,
    modelo_ia TEXT DEFAULT 'gpt-3.5-turbo',
    proveedor_ia TEXT DEFAULT 'OpenAI',
    activo INTEGER DEFAULT 1
  );
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:12
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:12
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:20
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:23:30.654
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:24:03.374
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:26:25.467
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:29:58.672
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:29:58.675
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:30:22.099
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:30:22.100
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:31:00.571
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:31:00.573
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:32:07.032
user: t7AI
action: ALTER
sql: |
  ALTER TABLE prueba_manual ADD COLUMN edad INTEGER;
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:32:07.034
user: t7AI
action: ALTER
sql: |
  ALTER TABLE prueba_manual ADD COLUMN edad INTEGER;
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:41:44.600
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:41:44.601
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:43:11.881
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 05:43:11.885
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: IF
date: 2025-05-01
time: 07:57:38.066
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 07:57:38.069
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 07:59:49.929
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 07:59:49.931
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 08:08:04.881
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS CLIENTES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 08:08:04.885
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS CLIENTES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 08:13:10.104
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 08:13:10.105
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 08:13:30.590
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 08:13:30.594
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 08:24:07.551
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 08:24:07.553
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 08:28:40.656
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 08:28:40.658
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:33:51.604
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:33:51.606
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:34:08.257
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:34:08.260
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:37:15.233
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:37:15.235
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: PRODUCTOS
date: 2025-05-01
time: 08:37:31.280
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: PRODUCTOS
date: 2025-05-01
time: 08:37:31.283
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: PRODUCTOS
date: 2025-05-01
time: 08:41:00.311
user: t7AI
action: DROP
sql: |
  DROP TABLE productos
```

```yaml
table: PRODUCTOS
date: 2025-05-01
time: 08:41:00.313
user: t7AI
action: DROP
sql: |
  DROP TABLE productos
```

```yaml
table: XEMPLEADOS
date: 2025-05-01
time: 08:41:14.276
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS xempleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: XEMPLEADOS
date: 2025-05-01
time: 08:41:14.279
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS xempleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: XEMPLEADOS
date: 2025-05-01
time: 08:48:07.502
user: t7AI
action: DROP
sql: |
  DROP TABLE xempleados
```

```yaml
table: XEMPLEADOS
date: 2025-05-01
time: 08:48:07.503
user: t7AI
action: DROP
sql: |
  DROP TABLE xempleados
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:48:30.447
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:48:30.449
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 08:58:15.275
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 08:58:35.365
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 08:58:35.367
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 09:03:56.202
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 09:03:56.204
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 09:04:09.458
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 09:04:09.460
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 09:08:12.475
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 09:08:27.765
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: CLIENTES
date: 2025-05-01
time: 09:08:27.767
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:15:55.178
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 09:16:42.817
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 09:16:42.822
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:19:11.687
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 09:19:29.529
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id entero autoincremental,
    nombre texto obligatorio
  );
```

```yaml
table: IF
date: 2025-05-01
time: 09:19:29.531
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id entero autoincremental,
    nombre texto obligatorio
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:30:56.530
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 09:31:08.558
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 09:31:08.560
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:35:36.446
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 09:35:36.447
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: IF
date: 2025-05-01
time: 09:36:15.860
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: IF
date: 2025-05-01
time: 09:36:15.864
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:46:20.368
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 09:46:20.369
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 09:46:32.593
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:46:32.595
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:55:10.879
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 09:55:10.882
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 09:55:21.678
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 09:55:21.681
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:06:37.248
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 10:06:55.538
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:31:32.358
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 10:31:46.717
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:31:46.720
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:32:16.217
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 10:33:31.151
user: t7AI
action: DROP
sql: |
  DROP TABLE prueba_manual
```

```yaml
table: prueba_manual
date: 2025-05-01
time: 10:33:32.964
user: t7AI
action: CREATE
sql: |
  CREATE TABLE prueba_manual (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  )
```

```yaml
table: clientes
date: 2025-05-01
time: 10:36:28.502
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:36:28.504
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:50:07.742
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 10:50:20.611
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:50:48.878
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 10:51:05.888
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: clientes
date: 2025-05-01
time: 10:55:18.772
user: t7AI
action: DROP
sql: |
  DROP TABLE CLIENTES
```

```yaml
table: clientes
date: 2025-05-01
time: 10:55:31.300
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

