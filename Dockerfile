# Image outil pour le package SIPC : validation JSON, lint doctrinal, tests et MkDocs.
# Toute exécution de l'outillage passe par ce conteneur (aucune installation hôte).
FROM python:3.12-slim

WORKDIR /sipc

# Dépendances d'abord pour profiter du cache de couches Docker.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Le code est monté en volume (voir docker-compose.yml) ; rien d'autre à copier.
EXPOSE 8000

CMD ["python", "tools/validate_json_files.py", "examples", "schemas"]
