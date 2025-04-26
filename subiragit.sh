#!/bin/bash

# 1. Toma el mensaje como argumento
MENSAJE="$1"

# 2. Verifica que haya mensaje
if [ -z "$MENSAJE" ]; then
  echo "⚠️  Especifica un mensaje de commit. Ejemplo: ./subiragit.sh \"mensaje de commit\""
  exit 1
fi

# 3. Detecta automáticamente la rama activa
RAMA=$(git branch --show-current)

# 4. Añade todos los cambios
git add .

# 5. Hace el commit
git commit -m "$MENSAJE"

# 6. Push a la rama detectada
git push origin "$RAMA"

# 7. Guarda el mensaje en un log
mkdir -p logs
echo "$(date '+%Y-%m-%d %H:%M:%S') - Rama: $RAMA - Mensaje: $MENSAJE" >> logs/git_push.log

# 8. Mensaje de confirmación
echo "✅ Cambios subidos a rama '$RAMA' con mensaje: '$MENSAJE'"