
from solutions.day03.solve import extract_pairs


class TestExtractPairs:

    def test_extracts_one_pair(self):
        assert extract_pairs('mul(1,1)') == [(1, 1)]
