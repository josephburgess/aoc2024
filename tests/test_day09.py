import pytest

from solutions.day09 import Disk, compact_disk, parse_disk_map, solve


@pytest.fixture
def example_data():
    return "2333133121414131402"


def test_parse_disk(example_data: str):
    assert parse_disk_map(example_data) == [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]


def test_compact_disk(example_data: str):
    disk_map = parse_disk_map(example_data)
    assert compact_disk(disk_map) == [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


def test_example_data(example_data: str):
    pass
