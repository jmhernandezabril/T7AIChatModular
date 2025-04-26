# Push a GitHub con token seguro

Este es el comando para hacer push con el token sin subirlo al repositorio:

```bash
source .env
git push https://$GITHUB_TOKEN@github.com/jmhernandezabril/T7AIChatModular.git
```

✅ El archivo `.env` está en `.gitignore`, así que nunca se subirá al repositorio.

🛡️ Si cambias el token, actualízalo en `.env`.
