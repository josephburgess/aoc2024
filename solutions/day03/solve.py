import re

from custom_types import Solution


def extract_pairs(data: str) -> list[tuple[int, int]]:
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches: list[tuple[str, str]] = re.findall(pattern, data)
    return [(int(x), int(y)) for x, y in matches]


def multiply_and_sum(pairs: list[tuple[int, int]]):
    return sum(x * y for x, y in pairs)


def solve(data: str) -> Solution:
    solution_one = multiply_and_sum(extract_pairs(data))
    return solution_one, 0
