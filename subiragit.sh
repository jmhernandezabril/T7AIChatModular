#!/bin/bash

# 1. Toma el mensaje como argumento
MENSAJE="$1"

# 2. Si no hay mensaje, pide uno
if [ -z "$MENSAJE" ]; then
  echo "⚠️  Especifica un mensaje de commit. Ejemplo: ./subiragit.sh \"mensaje\""
  exit 1
fi

# 3. Añade todos los cambios
git add .

# 4. Commit con mensaje
git commit -m "$MENSAJE"

# 5. Push
git push origin main

# 6. Registro en logs (opcional)
echo "$(date '+%Y-%m-%d %H:%M:%S') - $MENSAJE" >> logs/git_push.log

# 7. Confirmación
echo "✅ Cambios subidos con mensaje: $MENSAJE"
