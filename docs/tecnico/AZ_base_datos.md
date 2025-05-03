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

```yaml
table: clientes
date: 2025-05-01
time: 11:04:58.426
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-01
time: 11:05:05.336
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
date: 2025-05-03
time: 06:44:07.308
user: t7AI
action: DROP
sql: |
  DROP TABLE clientes
```

```yaml
table: clientes
date: 2025-05-03
time: 06:44:24.374
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    nombre TEXT
  );
```

```yaml
table: clientes
date: 2025-05-03
time: 06:52:38.438
user: t7AI
action: DROP
sql: |
  DROP TABLE CLIENTES
```

```yaml
table: clientes
date: 2025-05-03
time: 06:52:53.183
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
date: 2025-05-03
time: 06:54:51.870
user: t7AI
action: DROP
sql: |
  DROP TABLE CLIENTES
```

```yaml
table: clientes
date: 2025-05-03
time: 06:54:59.936
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: a
date: 2025-05-03
time: 07:03:56.482
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS a (
    id INTEGER PRIMARY KEY AUTOINCREMENT
  );
```

```yaml
table: obras
date: 2025-05-03
time: 07:44:29.762
user: t7AI
action: CREATE
sql: |
  CREATE TABLE obras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT,
    direccion TEXT,
    fecha_inicio TEXT,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
  );
```

```yaml
table: pruebam
date: 2025-05-03
time: 09:43:06.431
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebam (
    id INTEGER,
    nombre TEXT
  );
```

```yaml
table: x
date: 2025-05-03
time: 10:05:26.233
user: user1
action: CREATE
sql: |
  CREATE TABLE X(
    id INT
  )
```

```yaml
table: instrucciones
date: 2025-05-03
time: 10:27:24.922
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 12:40:21.135
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 12:48:14.977
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 12:53:22.426
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 12:53:53.262
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 12:59:59.367
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 13:48:01.928
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:01:14.978
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:03:09.863
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:05:21.842
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:07:44.137
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:11:07.649
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:12:50.069
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:15:42.768
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:17:20.656
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:20:03.104
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:21:36.121
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:25:24.522
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:27:44.953
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:32:56.803
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:36:12.171
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:39:31.210
user: u3
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: estoy_aqui
date: 2025-05-03
time: 14:49:50.798
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS estoy_aqui (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:49:58.323
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:55:42.888
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:56:44.583
user: t7AI
action: DROP
sql: |
  DROP TABLE INSTRUCCIONES
```

```yaml
table: instrucciones
date: 2025-05-03
time: 14:56:56.183
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    mensaje TEXT NOT NULL
  );
```

```yaml
table: instrucciones
date: 2025-05-03
time: 15:06:32.254
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS instrucciones (
    saludo TEXT NOT NULL
  );
```

```yaml
table: pruebax
date: 2025-05-03
time: 15:21:53.135
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaX (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  );
```

```yaml
table: pruebax
date: 2025-05-03
time: 15:22:02.458
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaX (
    id INTEGER PRIMARY KEY,
    nombr TEXT
  );
```

```yaml
table: pruebax
date: 2025-05-03
time: 15:22:23.467
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaX (
    id INTEGER PRIMARY KEY,
    nombre TEXT
  );
```

```yaml
table: pruebax
date: 2025-05-03
time: 15:24:41.570
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaX (
    id INTEGER,
    nombre TEXT
  );
```

```yaml
table: prueba11
date: 2025-05-03
time: 15:37:59.728
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS prueba11 (
    id INTEGER PRIMARY KEY,
    descripcion TEXT
  );
```

```yaml
table: pruebaxl
date: 2025-05-03
time: 15:41:45.992
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaXL (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    ampliacion TEXT
  );
```

```yaml
table: pruebaxl
date: 2025-05-03
time: 15:42:56.446
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaXL (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    ampliacion TEXT
  );
```

```yaml
table: pruebaxl
date: 2025-05-03
time: 15:48:55.539
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaxl (
    id INTEGER,
    nombre TEXT
  );
```

```yaml
table: pruebaxl
date: 2025-05-03
time: 15:50:56.661
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaxl (
    id INTEGER,
    nombre TEXT
  );
```

```yaml
table: pruebaxl99
date: 2025-05-03
time: 15:54:56.207
user: t7AI
action: CREATE
sql: |
  CREATE TABLE IF NOT EXISTS pruebaxl99 (
    id INTEGER,
    descripción TEXT
  );
```

```yaml
table: pruebaxl99
date: 2025-05-03
time: 15:58:18.954
user: t7AI
action: ALTER
sql: |
  ALTER TABLE pruebaxl99 ADD COLUMN NUEVACOLUMNA TEXT;
```

