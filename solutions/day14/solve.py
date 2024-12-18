import re


def parse_input(data: str) -> list[dict[str, int]]:
    robots: list[dict[str, int]] = []
    for line in data.strip().split("\n"):
        match = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append({'x': px, 'y': py, 'vx': vx, 'vy': vy})
    return robots


def move_robots(robots: list[dict[str, int]], time_steps: int, width: int, height: int) -> list[dict[str, int]]:
    for robot in robots:
        robot['x'] = (robot['x'] + robot['vx'] * time_steps) % width
        robot['y'] = (robot['y'] + robot['vy'] * time_steps) % height
    return robots


def count_robots_on_tiles(robots: list[dict[str, int]]) -> dict[tuple[int, int], int]:
    tile_counts: dict[tuple[int, int], int] = {}
    for robot in robots:
        position = (robot['x'], robot['y'])
        if position not in tile_counts:
            tile_counts[position] = 0
        tile_counts[position] += 1
    return tile_counts


def count_robots_in_quadrants(tile_counts: dict[tuple[int, int], int], width: int, height: int) -> tuple[int, int, int, int]:
    mid_x = width // 2
    mid_y = height // 2

    q1_count = sum(count for (x, y), count in tile_counts.items() if x < mid_x and y < mid_y)
    q2_count = sum(count for (x, y), count in tile_counts.items() if x > mid_x and y < mid_y)
    q3_count = sum(count for (x, y), count in tile_counts.items() if x < mid_x and y > mid_y)
    q4_count = sum(count for (x, y), count in tile_counts.items() if x > mid_x and y > mid_y)

    return q1_count, q2_count, q3_count, q4_count


def calculate_safety_factor(q1_count: int, q2_count: int, q3_count: int, q4_count: int) -> int:
    return q1_count * q2_count * q3_count * q4_count


def solve(data: str, width: int = 101, height: int = 103) -> tuple[int, int]:
    time_steps = 100
    robots = parse_input(data)
    moved_robots = move_robots(robots, time_steps, width, height)
    tile_counts = count_robots_on_tiles(moved_robots)
    q1_count, q2_count, q3_count, q4_count = count_robots_in_quadrants(tile_counts, width, height)
    safety_factor = calculate_safety_factor(q1_count, q2_count, q3_count, q4_count)

    return (safety_factor, 1)
