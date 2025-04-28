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

