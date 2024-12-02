import os
import importlib
from collections.abc import Callable

from custom_types import Solution


def main():
    solutions_path = "solutions"
    for folder in sorted(os.listdir(solutions_path)):
        folder_path = os.path.join(solutions_path, folder)

        if os.path.isdir(folder_path) and folder.startswith("day"):
            try:
                module = importlib.import_module(f"{solutions_path}.{folder}.solve")

                if hasattr(module, "solve"):
                    solve: Callable[[], Solution] = getattr(module, "solve")
                    results = solve()

                    print(f"\n{folder.capitalize()}")
                    print("=" * len(folder))
                    for key, value in results.items():
                        print(f"{key}: {value}")
                else:
                    print(f"{folder} needs a solve function!")
            except Exception as e:
                print(f"Error running {folder}: {e}")


if __name__ == "__main__":
    main()
