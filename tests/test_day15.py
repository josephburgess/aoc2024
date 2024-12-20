import pytest

from solutions.day15 import expand_warehouse, parse_input, run_warehouse_simulation, solve


@pytest.fixture
def example_data():
    return """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""


def test_small_data():

    small_data = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""
    assert solve(small_data) == (2028, 1)


def test_example_data(example_data: str):
    assert solve(example_data) == (10092, 9021)


def test_parse_map(example_data: str):
    grid, _ = parse_input(example_data)
    expanded_warehouse = expand_warehouse(grid)

    expanded_warehouse_str = "\n".join("".join(row) for row in expanded_warehouse)

    expected = """
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
""".strip()

    assert expanded_warehouse_str == expected


# def test_final_warehouse_state(example_data: str):
#     grid, moves = parse_input(example_data)
#     expanded_warehouse = expand_warehouse(grid)
#
#     _ = run_warehouse_simulation(expanded_warehouse, moves)
#
#     final_warehouse_str = "\n".join("".join(row) for row in expanded_warehouse)
#
#     expected = """
# ####################
# ##[].......[].[][]##
# ##[]...........[].##
# ##[]........[][][]##
# ##[]......[]....[]##
# ##..##......[]....##
# ##..[]............##
# ##..@......[].[][]##
# ##......[][]..[]..##
# ####################
# """.strip()
#
#     assert final_warehouse_str == expected
