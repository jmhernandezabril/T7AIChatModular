#!/bin/bash

# Mensaje automático de commit o solicita si no se pasa como argumento
COMMIT_MSG=$1
if [ -z "$COMMIT_MSG" ]; then
  echo "🔁 Escribe el mensaje del commit:"
  read COMMIT_MSG
fi

echo "🔄 Guardando cambios..."

# Guardar todo en Git
git add .
git commit -m "$COMMIT_MSG"

# Hacer pull con rebase y luego push con el token
git pull --rebase origin main
git push https://$GITHUB_TOKEN@github.com/jmhernandezabril/T7AIChatModular.git main

# Guardar salida en log
echo "[$(date)] Commit: $COMMIT_MSG" >> logs/git_push.log
