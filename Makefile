install:
	uv sync

build:
	uv build

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

check: test lint

lint-fix:
	uv run ruff check gendiff --fix

black:
	uv run black gendiff --target-version py312 gendiff