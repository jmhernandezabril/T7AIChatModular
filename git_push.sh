#!/bin/bash

echo "📝 Escribe el mensaje del commit:"
read mensaje

git add .
git commit -m "$mensaje"
git push https://$GITHUB_TOKEN@github.com/jmhernandezabril/T7AIChatModular.git