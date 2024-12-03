import re

from custom_types import Solution


def extract_pairs(data: str) -> list[tuple[int, int]]:
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches: list[tuple[str, str]] = re.findall(pattern, data)
    return [(int(x), int(y)) for x, y in matches]


def extract_conditional_pairs(data: str) -> list[tuple[int, int]]:
    pattern = r"(do\(\)|don't\(\)|mul\((\d+),\s*(\d+)\))"
    matches: list[tuple[str, str, str]] = re.findall(pattern, data)

    process_mul = True
    valid_pairs: list[tuple[int, int]] = []

    for match in matches:
        if match[0] == "do()":
            process_mul = True
        elif match[0] == "don't()":
            process_mul = False
        else:
            if process_mul and match[1] and match[2]:
                x = int(match[1])
                y = int(match[2])
                valid_pairs.append((x, y))

    return valid_pairs


def multiply_and_sum(pairs: list[tuple[int, int]]):
    return sum(x * y for x, y in pairs)


def solve(data: str) -> Solution:
    solution_one = multiply_and_sum(extract_pairs(data))
    solution_two = multiply_and_sum(extract_conditional_pairs(data))
    return solution_one, solution_two
