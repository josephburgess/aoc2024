import os
import importlib
from typing import Callable

def main():
    solutions_path = "solutions"
    for folder in sorted(os.listdir(solutions_path)):
        folder_path = os.path.join(solutions_path, folder)
        
        if os.path.isdir(folder_path) and folder.startswith("day"):
            try:
                module = importlib.import_module(f"{solutions_path}.{folder}.day01")
                
                if hasattr(module, "solve"):
                    solve: Callable[[], str] = getattr(module, "solve")
                    print(solve())
                else:
                    print(f"{folder} needs a solve function!")
            except Exception as e:
                print(f"Error running {folder}: {e}")

if __name__ == "__main__":
    main()
