.PHONY: install precommit-hooks build publish


install: ## Install dependencies with uv
	uv sync --all-extras --dev

precommit-hooks: ## Install pre-commit hooks
	uv run pre-commit install --install-hooks

build:
	uv lock
	uv build

publish: build
	uv publish
