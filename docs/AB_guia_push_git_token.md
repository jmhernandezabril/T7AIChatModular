**Guia paso a paso para automatizar el push a GitHub en Replit sin contraseña**

---

### ✅ Objetivo
Configurar un script en Replit que permita hacer `git add`, `git commit` y `git push` a GitHub sin pedir contraseña, usando un token seguro y dejando registro de los envíos.

---

### ⚡ Requisitos previos
- Tener un repositorio en GitHub creado.
- Tener una cuenta activa en Replit y tu proyecto abierto.

---

### 1. 🔐 Crear un token de acceso en GitHub

1. Ve a GitHub > Settings > Developer settings > Personal access tokens > Fine-grained tokens.
2. Crea uno nuevo con acceso solo a ese repositorio.
3. Marca permisos:
   - Repos: `contents: read/write`
4. Guarda el token (empieza por `ghp_...`) en un lugar seguro.

_(Ver imagen: `token_github_fine_grained.png`)_

---

### 2. 📂 Crear el archivo `.env` en Replit

1. En tu proyecto, crea un archivo nuevo llamado `.env` (sin extensión).
2. Dentro, pega:
   ```env
   GITHUB_TOKEN=ghp_tuTokenAqui123456789
   ```
3. Replit lo ocultará automáticamente por seguridad.

_(Ver imagen: `archivo_env_replit.png`)_

---

### 3. 🔢 Crear el script `subiragit.sh`

1. Crea un archivo llamado `subiragit.sh`
2. Contenido:
```bash
#!/bin/bash

mensaje="$1"
fecha=$(date '+%Y-%m-%d %H:%M:%S')
LOG_FILE="logs/git_push.log"

if [ -z "$mensaje" ]; then
  echo "⚠️ Especifica un mensaje. Uso: ./subiragit.sh \"tu mensaje\""
  exit 1
fi

# Guardar cambios
echo "📃 Guardando cambios..."
git add .
git commit -m "$mensaje"

git push https://${GITHUB_TOKEN}@github.com/tu_usuario/tu_repositorio.git main

# Registrar en log
echo "$fecha - Rama: main - Mensaje: '$mensaje'" >> $LOG_FILE

echo "✅ Cambios subidos con mensaje: '$mensaje'"
```

3. Dale permisos:
```bash
chmod +x subiragit.sh
```

_(Ver imagen: `script_push_token.png`)_

---

### 4. 🔍 Verificar funcionamiento

Cada vez que quieras hacer commit:
```bash
./subiragit.sh "mensaje bonito"
```

- El script hará `add`, `commit` y `push` directamente.
- Y dejará una línea en `logs/git_push.log` con la fecha y mensaje.

_(Ver imagen: `git_push_log.png`)_

---

### 💡 Consejo extra: alias opcional (no permanente)

Si quieres usar un alias corto dentro de una sesión:
```bash
alias gp='./subiragit.sh'
```
Y luego puedes ejecutar:
```bash
gp "mensaje corto"
```
(Solo mientras esté abierta la terminal)

---

### ✨ Resultado final
- Flujo de trabajo sin fricción.
- Seguridad mediante token en `.env`.
- Historial claro de cambios.
- Ideal para trabajar rápido en Replit.

---

¿Todo listo para trabajar con Git sin contraseñas cada vez? 🚀

