from textwrap import dedent

import pytest

from solutions.day06.solve import solve


@pytest.fixture
def example_data():
    return dedent("""
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
        """
                  )


def test_example_data(example_data: str):
    assert solve(example_data) == (41, 6)
