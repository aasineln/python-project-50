from typing import Any

from gendiff.formatters.stylish import format_stylish
from gendiff.scripts.file_parsers import parse_file


def get_diff(data1: dict[str, Any], data2: dict[str, Any]) -> dict[str, Any]:
    """
    Строит внутреннее представление различий между двумя словарями.

    Возвращает словарь, где для каждого ключа указан статус и значения:
    - "added": ключ только во втором словаре
    - "removed": ключ только в первом словаре
    - "unchanged": ключ в обоих словарях с одинаковыми значениями
    - "changed": ключ в обоих словарях с разными значениями
    - "nested": ключ в обоих словарях и значения - словари (рекурсивный обход)
    """
    all_keys = sorted(set(data1) | set(data2))
    result = {}

    for key in all_keys:
        if key not in data1:
            result[key] = {"status": "added", "value": data2[key]}
        elif key not in data2:
            result[key] = {"status": "removed", "value": data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                "status": "nested",
                "children": get_diff(data1[key], data2[key]),
            }
        elif data1[key] == data2[key]:
            result[key] = {"status": "unchanged", "value": data1[key]}
        else:
            result[key] = {
                "status": "changed",
                "old_value": data1[key],
                "new_value": data2[key],
            }

    return result


def generate_diff(
    file_path1: str, file_path2: str, format_type: str = "stylish"
) -> str:
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = get_diff(data1, data2)

    if format_type == "stylish":
        return format_stylish(diff)
    else:
        raise ValueError(f"Unsupported format: {format_type}")
