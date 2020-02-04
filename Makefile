PROJECT = sol
PUBLIC_SOURCES = $(wildcard $(PROJECT)/[^_]*.py)
PUBLIC_SUBMODULES = $(patsubst $(PROJECT)/%, $(PROJECT).%, $(PUBLIC_SOURCES))

install:
	@poetry install

test:
	@poetry run python -m unittest tests

doctest:
	poetry run python -m doctest $(PUBLIC_SUBMODULES)

doc:
	@pdoc --html -o docs sol

selfcheck:
	poetry check

check: selfcheck test

build: check
	@poetry build

.PHONY: install test selfcheck check build
