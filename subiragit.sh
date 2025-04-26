#!/bin/bash

# 1. Cargar variables de entorno
source .env

# 2. Leer mensaje de commit
MENSAJE="$1"

# 3. Verificar que haya mensaje
if [ -z "$MENSAJE" ]; then
  echo "⚠️  Especifica un mensaje. Ejemplo: ./subiragit.sh \"mensaje bonito\""
  exit 1
fi

# 4. Detectar rama actual
RAMA=$(git branch --show-current)

# 5. Mostrar mensaje de inicio
echo "🟢 Guardando cambios en rama '$RAMA'..."

# 6. Añadir todos los cambios
git add .

# 7. Crear commit
git commit -m "$MENSAJE"

# 8. Sincronizar primero para evitar conflictos
git pull --rebase origin "$RAMA"

# 9. Hacer push usando token
git push https://${GITHUB_TOKEN}@github.com/jmhernandezabril/T7AIChatModular.git "$RAMA"

# 10. Crear carpeta de logs si no existe
mkdir -p logs

# 11. Guardar en logs
echo "$(date '+%Y-%m-%d %H:%M:%S') - $MENSAJE" >> logs/git_push.log

# 12. Mensaje de confirmación
echo "✅ Cambios subidos correctamente a '$RAMA' con el mensaje: '$MENSAJE'"