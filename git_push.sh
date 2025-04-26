#!/bin/bash

# Cargar variables del entorno
source .env

# Mensaje del commit como argumento
mensaje="$1"

# Ruta del log
LOG_FILE="logs/git_push.log"

# Fecha actual
fecha=$(date "+%Y-%m-%d %H:%M:%S")

# Mostrar mensaje
echo "🟢 Guardando cambios..."

# Añadir todos los cambios
git add .

# Hacer el commit
git commit -m "$mensaje"

# Hacer push con token desde variable de entorno
git push https://$GITHUB_TOKEN@github.com/jmhernandezabril/T7AIChatModular.git main

# Guardar en log
echo "[$fecha] $mensaje" >> $LOG_FILE