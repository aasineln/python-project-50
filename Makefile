install:
	uv sync

build:
	uv build

run:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

lint-fix:
	uv run ruff check gendiff --fix

black:
	uv run black gendiff --target-version py312 gendiff