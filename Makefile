# Raccourcis SIPC — tout s'exécute dans le conteneur Docker (jamais en local).
DC = docker compose run --rm sipc

.PHONY: build validate lint test check serve docs clean

build:            ## Construit l'image Docker outillée
	docker compose build

validate:         ## Valide les exemples JSON contre les schémas
	$(DC) python tools/validate_json_files.py examples schemas

lint:             ## Applique le linter doctrinal SIPC sur les exemples
	$(DC) python tools/check_doctrine.py examples

test:             ## Lance la suite pytest
	$(DC) pytest -q

check: validate lint test   ## Validation + lint + tests

docs:             ## Construit le site MkDocs en mode strict
	$(DC) mkdocs build --strict

serve:            ## Sert le site localement sur http://localhost:8000
	docker compose run --rm --service-ports sipc mkdocs serve -a 0.0.0.0:8000

clean:            ## Supprime le site généré
	rm -rf site
