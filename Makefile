env:
	poetry install

test:
	poetry run pytest

lint:
	poetry run isort . --check-only
	poetry run black . --check --diff
	poetry run flake8