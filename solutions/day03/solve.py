import re


def extract_pairs(data: str) -> list[tuple[int, int]]:
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches: list[tuple[str, str]] = re.findall(pattern, data)
    return [(int(x), int(y)) for x, y in matches]
