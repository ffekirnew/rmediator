.phony: format lint test test-coverage build upload

format:
	@echo "Make: Running formatters..."
	@isort src
	@black src

lint:
	@echo "Make: Running linters..."
	@ruff check src

test:
	@echo "Make: Running tests..."
	@pytest

test-coverage:
	@echo "Make: Running tests with coverage..."
	@coverage run -m pytest -q
	@coverage report -m

build:
	@echo "Make: Building package..."
	@python3 -m pip install build
	@python3 -m build --wheel

upload: build
	@echo "Make: Uploading package..."
	@twine upload dist/*
	@rm -rf dist
	@rm -rf build
	@rm -rf *.egg-info
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@rm -rf .eggs
	@rm -rf .tox
