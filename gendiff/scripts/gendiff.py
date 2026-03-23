import json
from typing import Any
from pathlib import Path


def parse_json(file_path: str) -> dict[str, Any]:
    path = Path("gendiff", "data", file_path)
    with open(path, "r") as file:
        return json.load(file)


def build_diff(data1: dict[str, Any], data2: dict[str, Any]) -> dict[str, Any]:
    all_keys = sorted(set(data1) | set(data2))

    def get_status(key: str) -> str:
        if key not in data1:
            return "added"
        if key not in data2:
            return "removed"
        if data1[key] == data2[key]:
            return "unchanged"
        return "changed"

    return {
        key: {
            "status": get_status(key),
            "value1": data1.get(key),
            "value2": data2.get(key),
        }
        for key in all_keys
    }


def format_diff(diff: dict[str, Any]) -> str:
    lines = ["{"]

    for key, value in diff.items():
        status = value["status"]

        if status == "unchanged":
            lines.append(f'    {key}: {value["value1"]}')
        elif status == "removed":
            lines.append(f'  - {key}: {value["value1"]}')
        elif status == "added":
            lines.append(f'  + {key}: {value["value2"]}')
        elif status == "changed":
            lines.append(f'  - {key}: {value["value1"]}')
            lines.append(f'  + {key}: {value["value2"]}')

    lines.append("}")
    return "\n".join(lines)


def generate_diff(file_path1: str, file_path2: str) -> str:
    data1 = parse_json(file_path1)
    data2 = parse_json(file_path2)

    diff = build_diff(data1, data2)
    return format_diff(diff)
