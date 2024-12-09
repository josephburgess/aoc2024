import argparse
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

_ = load_dotenv()
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
BASE_URL = "https://adventofcode.com/2024/day/{day}/input"
INPUT_DIR = Path(__file__).parent.parent / "input"
SOLUTIONS_DIR = Path(__file__).parent.parent / "solutions"
TESTS_DIR = Path(__file__).parent.parent / "tests"


def fetch_input(day: int):
    """Fetch and save the input file for the given day."""
    url = BASE_URL.format(day=day)
    headers = {"Cookie": f"session={SESSION_COOKIE}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        INPUT_DIR.mkdir(parents=True, exist_ok=True)
        input_file = INPUT_DIR / f"day{day:02}.txt"
        with open(input_file, "w") as f:
            _ = f.write(response.text)
        print(f"input day {day} saved to {input_file}")
    else:
        print(f"error fetching input day {day}: {response.status_code}")
        response.raise_for_status()


def create_solution_files(day: int):
    day_dir = SOLUTIONS_DIR / f"day{day:02}"
    day_dir.mkdir(parents=True, exist_ok=True)

    init_file = day_dir / "__init__.py"
    if not init_file.exists():
        with open(init_file, "w") as f:
            _ = f.write("from .solve import *\n")
        print(f"created {init_file}")

    solve_file = day_dir / "solve.py"
    code = (
        f'def solve(data: str):\n'
        f'    pass\n'
    )

    if not solve_file.exists():
        with open(solve_file, "w") as f:
            _ = f.write(code)
        print(f"Created {solve_file}")


def create_test_file(day: int):
    test_file = TESTS_DIR / f"test_day{day:02}.py"
    TESTS_DIR.mkdir(parents=True, exist_ok=True)

    code = (
        f'import pytest\n\n'
        f'from solutions.day{day:02} import solve\n\n\n'
        f'@pytest.fixture\n'
        f'def example_data():\n'
        f'    pass\n\n\n'
        f'def test_example_data(example_data: str):\n'
        f'    pass\n'
    )
    if not test_file.exists():
        with open(test_file, "w") as f:
            _ = f.write(code)
        print(f"Created {test_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("day", type=int, help="The day of the Advent of Code challenge to set up")
    args = parser.parse_args()
    day = int(args.day)

    try:
        print(f"Setting up for Day {day:02}")
        fetch_input(day)
        create_solution_files(day)
        create_test_file(day)
        print(f"Setup complete for Day {day:02}!")
    except Exception as e:
        print(f"Error during setup: {e}")
