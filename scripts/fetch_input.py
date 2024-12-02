import os
import requests
from pathlib import Path
from dotenv import load_dotenv
import argparse


_ = load_dotenv()
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
BASE_URL = "https://adventofcode.com/2024/day/{day}/input"
INPUT_DIR = Path(__file__).parent.parent / "input"


def fetch_input(day: int):
    url = BASE_URL.format(day=day)
    headers = {"Cookie": f"session={SESSION_COOKIE}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        INPUT_DIR.mkdir(parents=True, exist_ok=True)
        input_file = INPUT_DIR / f"day{day:02}.txt"
        with open(input_file, "w") as f:
            _ = f.write(response.text)
        print(f"Input for day {day} saved to {input_file}")
    else:
        print(f"failed to fetch: {response.status_code}")
        response.raise_for_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("day", type=int)
    args = parser.parse_args()
    fetch_input(args.day)
