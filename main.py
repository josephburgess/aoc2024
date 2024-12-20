import importlib
import sys
from collections.abc import Callable
from pathlib import Path

from custom_types import Pair
from utils import print_solutions


def main():
    solutions_path, input_path = Path("solutions"), Path("input")

    specific_day = None
    if len(sys.argv) > 1:
        try:
            day_number = int(sys.argv[1])
            specific_day = f"day{day_number:02d}"
        except ValueError:
            print("invalid day format")
            return

    day_folders = [f for f in solutions_path.iterdir() if f.is_dir() and f.name.startswith("day")]
    day_folders.sort()

    if specific_day:
        day_folders = [f for f in day_folders if f.name == specific_day]

    for folder in day_folders:
        input_file = input_path / f"{folder.name}.txt"

        if not input_file.exists():
            print(f"Input file for {folder.name} missing")
            continue

        try:
            data = input_file.read_text()
            module = importlib.import_module(f"{solutions_path}.{folder.name}.solve")
            solve: Callable[[str], Pair] = getattr(module, "solve")
            solution = solve(data)
            print_solutions(folder.name, solution)

        except Exception as e:
            print(f"Error in {folder.name}: {e}")


if __name__ == "__main__":
    main()
