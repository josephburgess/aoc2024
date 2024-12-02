from .logic import is_safe_report, parse_arrays

def solve():
    with open("input/day02.txt", "r") as f:
        data = f.read()

    reports = parse_arrays(data)

    count = 0
    for r in reports:
        if is_safe_report(r):
            count += 1

    print(count)
