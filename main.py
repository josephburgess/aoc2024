import importlib
from typing import Callable
from pathlib import Path
from custom_types import Solution


def main():
    solutions_path = "solutions"
    input_path = "input"
    for folder in sorted(Path(solutions_path).iterdir()):
        if folder.is_dir() and folder.name.startswith("day"):
            try:
                input_file = Path(input_path) / f"{folder.name}.txt"
                if not input_file.exists():
                    print(f"input file for {folder.name} missing")
                    continue

                with input_file.open("r") as f:
                    data = f.read()

                module = importlib.import_module(f"{solutions_path}.{folder.name}.solve")

                if hasattr(module, "solve"):
                    solve: Callable[[str], Solution] = getattr(module, "solve")
                    results = solve(data)

                    print(f"\n{folder.name.capitalize()}")
                    print("=" * len(folder.name))
                    for i, answer in enumerate(results, start=1):
                        print(f"Answer {i}: {answer}")
                else:
                    print(f"{folder.name} needs a solve function!")
            except Exception as e:
                print(f"Error {folder.name}: {e}")


if __name__ == "__main__":
    main()
