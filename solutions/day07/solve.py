from custom_types import Pair

type Equation = tuple[int, list[int]]


def parse_input(data: str) -> list[Equation]:
    equations: list[Equation] = []
    for line in data.strip().splitlines():
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def concatenate(a: int, b: int) -> int:
    return int(f"{a}{b}")


def can_produce_target(target: int, numbers: list[int], concatenate: bool = False) -> bool:
    def dfs(current_value: int, i: int) -> bool:
        if i == len(numbers):
            return current_value == target

        if dfs(add(current_value, numbers[i]), i + 1):
            return True

        if dfs(multiply(current_value, numbers[i]), i + 1):
            return True

        if concatenate:
            if dfs(concatenate(current_value, numbers[i]), i + 1):
                return True

        return False

    return dfs(numbers[0], 1)


def solve(data: str) -> Pair:
    equations = parse_input(data)
    test_values: list[int] = []
    test_values_two: list[int] = []
    for e in equations:
        target, numbers = e
        if can_produce_target(target, numbers):
            test_values.append(target)
        if can_produce_target(target, numbers, concatenate=True):
            test_values_two.append(target)
    return (sum(test_values), sum(test_values_two))

# compute_possible_values(numbers)recursive? -> set of possible results if one number return set of one
# return possible_values
# can_produce_target(target, numbers) -> bool - is target in list of possible vals
# add(a, b) -> int
# multiply(a, b) -> int
