from textwrap import dedent

import pytest

from solutions.day10.solve import find_trailheads, parse_trail_map, solve


@pytest.fixture
def example_data():
    return dedent(
        """
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
        """
    )


def test_parse_trail_map():
    data = dedent("""
        0123
        1234
        8765
        9876
    """)
    trail_map = parse_trail_map(data)
    assert find_trailheads(trail_map) == [(0, 0)]


def test_example_data(example_data: str):
    assert solve(example_data) == (36, 1)
