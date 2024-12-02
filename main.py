import importlib
from collections.abc import Callable
from pathlib import Path

from custom_types import Solution
from solutions.utils import print_solutions


def main():
    solutions_path, input_path = Path("solutions"), Path("input")

    for folder in sorted(solutions_path.iterdir()):
        if folder.is_dir() and folder.name.startswith("day"):
            input_file = input_path / f"{folder.name}.txt"

            if not input_file.exists():
                print(f"Input file for {folder.name} missing")
                continue

            try:
                data = input_file.read_text()
                module = importlib.import_module(f"{solutions_path}.{folder.name}.solve")
                solve: Callable[[str], Solution] = getattr(module, "solve")
                solution = solve(data)
                print_solutions(folder.name, solution)

            except Exception as e:
                print(f"Error in {folder.name}: {e}")


if __name__ == "__main__":
    main()

