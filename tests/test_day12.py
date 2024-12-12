from textwrap import dedent

import pytest

from solutions.day12 import solve


@pytest.fixture
def example_data():
    return dedent("""
        RRRRIICCFF
        RRRRIICCCF
        VVRRRCCFFF
        VVRCCCJFFF
        VVVVCJJCFE
        VVIVCCJJEE
        VVIIICJJEE
        MIIIIIJJEE
        MIIISIJEEE
        MMMISSJEEE
        """
                  )


def test_example_data(example_data: str):
    assert solve(example_data) == (1930, 1)
