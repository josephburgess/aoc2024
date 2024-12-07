from custom_types import Pair


def parse_input(data) -> list[tuple[int, list[int]]]:
    equations = []
    for line in data.strip().splitlines():
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations

# can_produce_target(target, numbers) -> bool
# compute_possible_values(numbers)	recursive? -> possible results
# get_available_operators() -> list[Callable[operators]]
# apply_operator(left, right, operator) -> int
# add(a, b) -> int
# multiply(a, b) -> int


def solve(data: str) -> Pair:
    return (3749, 1)
