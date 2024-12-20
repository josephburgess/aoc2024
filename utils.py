from typing import Callable

from custom_types import Pair


def split_and_map(data: str, sep: str | None = None, func: Callable[[str], int] = int) -> list[list[int]]:
    return [list(map(func, line.split(sep))) for line in data.strip().splitlines()]


def print_solutions(folder_name: str, solution: Pair) -> None:
    print(f"\n{folder_name.capitalize()}")
    print("=" * len(folder_name))
    for i, answer in enumerate(solution, start=1):
        print(f"Answer {i}: {answer}")


def parse_grid(data: str):
    return [list(row.strip()) for row in data.strip().splitlines()]
