#!/bin/bash

# Cargar el token desde .env
source .env

# Mensaje del commit
mensaje=$1

# Verifica si el remote ya contiene el token
expected_url="https://${GITHUB_TOKEN}@github.com/jmhernandezabril/T7AIChatModular.git"
current_url=$(git remote get-url origin)

if [[ "$current_url" != "$expected_url" ]]; then
  echo "🔧 Actualizando remote origin con token..."
  git remote set-url origin "$expected_url"
fi

echo "💾 Guardando cambios..."
git add .
git commit -m "$mensaje"
git push origin main