from typing import Any


def format_value(value: Any, depth: int = 0) -> str:
    indent = "    " * (depth + 1)

    if isinstance(value, dict):
        lines = ["{"]
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return str(value)


def format_stylish(diff: dict[str, Any], depth: int = 0) -> str:
    indent = "    " * depth
    lines = ["{"]

    for key, node in diff.items():
        status = node["status"]

        if status == "nested":
            lines.append(
                f"{indent}    {key}: "
                f"{format_stylish(node["children"], depth + 1)}"
            )
        elif status == "added":
            value = format_value(node["value"], depth)
            lines.append(f"{indent}  + {key}: {value}")
        elif status == "removed":
            value = format_value(node["value"], depth)
            lines.append(f"{indent}  - {key}: {value}")
        elif status == "unchanged":
            value = format_value(node["value"], depth)
            lines.append(f"{indent}    {key}: {value}")
        elif status == "changed":
            old_value = format_value(node["old_value"], depth)
            new_value = format_value(node["new_value"], depth)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")

    lines.append(f"{indent}}}")
    return "\n".join(lines)
