from .logic import is_safe_report, is_valid_with_removal, parse_arrays

def solve():
    with open("input/day02.txt", "r") as f:
        data = f.read()

    reports = parse_arrays(data)

    count = sum(is_safe_report(r) for r in reports)

    safer_count = sum(is_valid_with_removal(r) for r in reports)

    return (f"\nDay 2\n"
            f"=======\n"
            f"1) Safe reports: {count}\n"
            f"2) more accurate count: {safer_count}\n")
