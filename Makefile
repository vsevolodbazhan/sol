install:
	@poetry install

test:
	@poetry run python -m unittest

doc:
	@poetry run pdoc --html -o docs sol

selfcheck:
	@poetry check

check: selfcheck test

build: check
	@poetry build

.PHONY: install test selfcheck check build
