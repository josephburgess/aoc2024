import pytest

from solutions.day02.logic import is_safe_report, is_valid_with_removal, parse_arrays


class TestParseLists:
    def test_single_line(self):
        data = "1 2 3 4"
        result = parse_arrays(data)
        assert result == [[1, 2, 3, 4]]

    def test_multiple_lines(self):
        data = """
        1 2 3 4
        5 6 7 8
        """
        result = parse_arrays(data)
        assert result == [[1, 2, 3, 4], [5, 6, 7, 8]]

    def test_empty_input(self):
        data = ""
        result = parse_arrays(data)
        assert result == []


class TestLevelSafety:
    def test_safe_report_ascending(self):
        data = [1, 2, 3, 4, 5]
        assert is_safe_report(data)

    def test_safe_report_descending(self):
        data = [5, 4, 3, 2, 1]
        assert is_safe_report(data)

    def test_safe_report_large_gap(self):
        data = [1, 2, 3, 9, 10]
        assert not is_safe_report(data)

    def test_safe_report_when_number_unchanged(self):
        data = [1, 2, 3, 3, 4]
        assert not is_safe_report(data)

    def test_increasing_with_gap_out_of_range(self):
        data = [1, 2, 3, 7]
        assert not is_safe_report(data)

    def test_decreasing_with_gap_out_of_range(self):
        data = [10, 8, 6, 1]
        assert not is_safe_report(data)

    def test_inconsistent_order(self):
        data = [1, 2, 3, 2, 1]
        assert not is_safe_report(data)

    def test_gaps_out_of_order(self):
        data = [10, 7, 5, 11]
        assert not is_safe_report(data)


class TestIsValidWithRemoval:
    def test_is_valid_with_removal(self):
        # just using examples from the puzzle to verify for Q2
        assert is_valid_with_removal([7, 6, 4, 2, 1])
        assert not is_valid_with_removal([1, 2, 7, 8, 9])
        assert not is_valid_with_removal([9, 7, 6, 2, 1])
        assert is_valid_with_removal([1, 3, 2, 4, 5])
        assert is_valid_with_removal([8, 6, 4, 4, 1])
        assert is_valid_with_removal([1, 3, 6, 7, 9])


@pytest.fixture
def real_data():
    with open("input/day02.txt", "r") as f:
        return f.read()


class TestSolve:

    def test_solve_first_puzzle(self, real_data: str):
        reports = parse_arrays(real_data)
        count = sum(is_safe_report(r) for r in reports)
        assert count == 220

    def test_solve_second_puzzle(self, real_data: str):
        reports = parse_arrays(real_data)
        count = sum(is_valid_with_removal(r) for r in reports)
        assert count == 296
