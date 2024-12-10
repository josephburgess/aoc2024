import pytest

from solutions.day09 import compact_disk, compact_disk_defrag, parse_disk_map, solve


@pytest.fixture
def example_data():
    return "2333133121414131402"


@pytest.fixture
def real_data():
    with open("input/day09.txt", "r") as f:
        return f.read()


def test_parse_disk(example_data: str):
    assert parse_disk_map(example_data) == [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]


def test_compact_disk(example_data: str):
    disk_map = parse_disk_map(example_data)
    assert compact_disk(disk_map) == [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


def test_compact_defrag(example_data: str):
    disk_map = parse_disk_map(example_data)
    assert compact_disk_defrag(disk_map) == [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, '.', 4, 4, '.', 3, 3, 3, '.', '.', '.', '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', '.', '.', '.', '.', 8, 8, 8, 8, '.', '.',]


def test_example_data(example_data: str):
    assert solve(example_data) == (1928, 2858)


@pytest.mark.skip  # skipping to save runtime
def test_real_data(real_data: str):
    assert solve(real_data) == (6386640365805, 6423258376982)
