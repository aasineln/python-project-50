import json
from pathlib import Path
from typing import Any

import yaml

BASE_PATH = Path("tests", "test_data")


def parse_json(file_path: str) -> dict[str, Any]:
    with open(BASE_PATH / file_path, "r") as file:
        return json.load(file)


def parse_yaml(file_path: str) -> dict[str, Any]:
    with open(BASE_PATH / file_path, "r") as file:
        return yaml.safe_load(file)


def get_parser(file_path: str):
    ext = Path(file_path).suffix.lower()

    if ext in [".json"]:
        return parse_json
    elif ext in [".yml", ".yaml"]:
        return parse_yaml
    raise ValueError(
        f"Unsupported file format: {ext}. Supported formats: .json, .yml, .yaml"
    )


def parse_file(file_path: str) -> dict[str, Any]:
    parser = get_parser(file_path)
    return parser(file_path)
