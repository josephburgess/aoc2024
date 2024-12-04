
def parse_grid(data: str):
    return [list(row.strip()) for row in data.strip().splitlines()]


def count_xmas(grid: list[list[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    word = "XMAS"
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    def dfs(row: int, col: int, index: int, row_step: int, col_step: int) -> bool:
        if index == len(word):
            return True
        if not (0 <= row < ROWS and 0 <= col < COLS):
            return False
        if grid[row][col] != word[index]:
            return False
        return dfs(row + row_step, col + col_step, index + 1, row_step, col_step)

    count = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == word[0]:
                for row_step, col_step in directions:
                    if dfs(row, col, 0, row_step, col_step):
                        count += 1
    return count


def solve(data: str):
    xmas_count = count_xmas(parse_grid(data))
    return (xmas_count, 1)
