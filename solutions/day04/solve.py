
def parse_grid(data: str):
    return [list(row.strip()) for row in data.strip().splitlines()]


def count_xmas(grid: list[list[str]]) -> int:
    word = "XMAS"
    ROWS, COLS = len(grid), len(grid[0])
    count = 0

    for row in grid:
        row_str = "".join(row)
        if word in row_str:
            count += 1

    for col in range(COLS):
        col_str = "".join(grid[row][col] for row in range(ROWS))
        if word in col_str:
            count += 1

    return count


def solve(data: str):
    xmas_count = count_xmas(parse_grid(data))
    return (xmas_count, 1)
