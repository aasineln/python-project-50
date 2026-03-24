from typing import Any


def format_plain(diff: dict[str, Any], path: str = "") -> str:
    lines = []

    for key, node in diff.items():
        current_path = f"{path}.{key}" if path else key
        status = node["status"]

        if status == "nested":
            lines.append(format_plain(node["children"], current_path))
        elif status == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif status == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif status == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return "\n".join(lines)


def format_value(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return str(value)
