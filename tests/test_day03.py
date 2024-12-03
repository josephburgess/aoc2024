
from solutions.day03.solve import extract_pairs


class TestExtractPairs:

    def test_extracts_one_pair(self):
        assert extract_pairs('mul(1,1)') == [(1, 1)]

    def test_extracts_two_pairs(self):
        assert extract_pairs('mul(1,1)mul(2,2)') == [(1, 1), (2, 2)]
