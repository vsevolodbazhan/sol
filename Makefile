PACKAGE = solists
DOCS = docs

install:
	@poetry install

test:
	@poetry run python -m unittest

doc:
	@poetry run pdoc --force --html -o $(DOCS) $(PACKAGE)
	@mv $(DOCS)/$(PACKAGE)/* ./$(DOCS)
	@rm -r $(DOCS)/$(PACKAGE)

selfcheck:
	@poetry check

check: selfcheck test

build: check
	@poetry build

.PHONY: install test selfcheck check build
