import re

from custom_types import Pair


def extract_pairs(data: str) -> list[Pair]:
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches: list[tuple[str, str]] = re.findall(pattern, data)
    return [(int(x), int(y)) for x, y in matches]


def extract_conditional_pairs(data: str) -> list[Pair]:
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),\s*(\d+)\))"
    matches: list[tuple[str, str, str]] = re.findall(pattern, data)
    process_mul = True
    valid_pairs: list[Pair] = []

    for match, x, y in matches:
        if match == "do()":
            process_mul = True
        elif match == "don't()":
            process_mul = False
        elif process_mul and x and y:
            valid_pairs.append((int(x), int(y)))

    return valid_pairs


def multiply_and_sum(pairs: list[Pair]):
    return sum(x * y for x, y in pairs)


def solve(data: str) -> Pair:
    solution_one = multiply_and_sum(extract_pairs(data))
    solution_two = multiply_and_sum(extract_conditional_pairs(data))
    return solution_one, solution_two
