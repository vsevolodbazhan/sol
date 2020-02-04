install:
	@poetry install

test:
	@poetry run python -m unittest

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test selfcheck check build
