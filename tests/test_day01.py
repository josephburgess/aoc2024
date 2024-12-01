import pytest
from solutions.day01 import parse_arrays, calculate_distance, calculate_similarity_score


@pytest.fixture
def test_data():
    return """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """


class TestParseArrays:

    def test_returns_tuple_of_arrays(self, test_data: str):
        result = parse_arrays(test_data)

        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], list)
        assert isinstance(result[1], list)

    def test_parses_correct_arrays(self, test_data: str):
        result = parse_arrays(test_data)

        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]

        assert result[0] == left
        assert result[1] == right


class TestCalculateDistance:

    def test_single_element_lists(self):
        left = [1]
        right = [1]
        result = calculate_distance(left, right)
        assert result == 0

    def test_single_element_different_lists(self):
        left = [2]
        right = [5]
        result = calculate_distance(left, right)
        assert result == 3

    def test_unsorted_lists(self):
        left = [3, 1, 2]
        right = [6, 4, 5]
        result = calculate_distance(left, right)
        assert result == 9

    def test_example_data(self, test_data: str):
        left, right = parse_arrays(test_data)

        result = calculate_distance(left, right)

        assert result == 11


class TestCalculateSimilarityScore:

    def test_calculate_similarity_score(self):
        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]

        result = calculate_similarity_score(left, right)

        assert result == 31
