from .logic import is_safe_report, parse_arrays

def solve():
    with open("input/day02.txt", "r") as f:
        data = f.read()

    reports = parse_arrays(data)

    count = 0
    safer_count = 0
    for r in reports:
        if is_safe_report(r):
            count += 1
            safer_count +=1
        else:
            for index in range(len(r)):
                modified_report = r[:index] + r[index + 1:]
                if is_safe_report(modified_report):
                    safer_count += 1
                    break

    return (f"\nDay 2\n"
            f"=======\n"
            f"1) Safe reports: {count}\n"
            f"2) more accurate count: {safer_count}\n")
