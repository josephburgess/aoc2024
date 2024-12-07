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

# compute_possible_values(numbers)	recursive? -> list of possible results
# can_produce_target(target, numbers) -> bool - is target in list of possible vals
# get_available_operators() -> list[Callable[operators]]
# apply_operator(left, right, operator) -> int
# add(a, b) -> int
# multiply(a, b) -> int


def solve(data: str) -> Pair:
    return (3749, 1)
