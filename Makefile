.PHONY: help setup test lint docker-build docker-test spec-check clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup:  ## Install dependencies
	pip install --upgrade pip
	pip install -r requirements-dev.txt

test: docker-build  ## Run tests in Docker
	docker run --rm chimera-factory

lint:  ## Run ruff lint + format
	ruff check --fix .
	ruff format .

docker-build:  ## Build Docker image
	docker build -t chimera-factory .

docker-test:  ## Run tests inside Docker
	docker run --rm chimera-factory

spec-check:  ## Verify repo aligns with specs
	python scripts/spec_check.py

clean:  ## Clean up
	rm -rf .venv __pycache__ *.egg-info .pytest_cache .ruff_cache