.phony: test build upload

test:
	@echo "Running tests..."
	@pytest

test-coverage:
	@echo "Running tests with coverage..."
	@coverage run -m pytest -q
	@coverage report -m

build:
	@echo "Building package..."
	@python setup.py sdist

upload:
	@echo "Uploading package..."
	@twine upload dist/*
	@rm -rf dist
	@rm -rf build
	@rm -rf *.egg-info
	@rm -rf .pytest_cache
	@rm -rf .coverage
	@rm -rf .eggs
	@rm -rf .tox
