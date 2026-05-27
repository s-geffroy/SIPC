# Raccourcis SIPC — tout s'exécute dans le conteneur Docker (jamais en local).
DC = docker compose run --rm sipc
LATEX = docker compose run --rm latex

.PHONY: build validate lint test check serve docs paper clean

build:            ## Construit l'image Docker outillée
	docker compose build

validate:         ## Valide les exemples JSON contre les schémas
	$(DC) python tools/validate_json_files.py examples schemas

lint:             ## Applique le linter doctrinal SIPC sur les exemples
	$(DC) python tools/check_doctrine.py examples

test:             ## Lance la suite pytest
	$(DC) pytest -q

check: validate lint test   ## Validation + lint + tests

paper:            ## Compile le papier LaTeX en PDF et le place dans docs/assets/
	$(LATEX) latexmk -pdf -interaction=nonstopmode -halt-on-error -cd paper/sipc_paper.tex
	mkdir -p docs/assets
	cp paper/sipc_paper.pdf docs/assets/sipc_paper.pdf

docs: paper       ## Compile le papier puis construit le site MkDocs en mode strict
	$(DC) mkdocs build --strict

serve:            ## Sert le site localement sur http://localhost:8000
	docker compose run --rm --service-ports sipc mkdocs serve -a 0.0.0.0:8000

clean:            ## Supprime le site généré et les artefacts LaTeX
	rm -rf site docs/assets/sipc_paper.pdf
	$(LATEX) latexmk -C -cd paper/sipc_paper.tex || true
