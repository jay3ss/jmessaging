.PHONY: help clean clean-build clean-pyc clean-test test init init-dev format coverage publish publish-test build
TEST_PATH=./

help:
	@echo "make init"
	@echo "		intialize the project for development"
	@echo "make clean"
	@echo "		remove python artifacts"
	@echo "make test"
	@echo "		run tests"

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

test: clean
	py.test --verbose --color=yes $(TEST_PATH)

init:
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

format:
	black .

coverage:
	coverage run -m pytest
	coverage report
	coverage html

build:
	python -m build --no-isolation --sdist --wheel

publish:
	python -m twine upload -r pypi dist/* --verbose

publish-test:
	python -m twine upload pypitest dist/* --verbose
