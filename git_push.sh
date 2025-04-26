#!/bin/bash

COMMIT_MSG=$1
if [ -z "$COMMIT_MSG" ]; then
  echo "🔁 Escribe el mensaje del commit:"
  read COMMIT_MSG
fi

echo "🔄 Guardando cambios..."

git add .
git commit -m "$COMMIT_MSG"
git pull --rebase origin main

# Push con token expandido
git push "https://${GITHUB_TOKEN}@github.com/jmhernandezabril/T7AIChatModular.git" main

echo "[$(date)] Commit: $COMMIT_MSG" >> logs/git_push.log
