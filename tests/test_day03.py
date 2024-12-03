
from solutions.day03.solve import extract_pairs, multiply_and_sum


class TestExtractPairs:

    def test_extracts_one_pair(self):
        assert extract_pairs('mul(1,1)') == [(1, 1)]

    def test_extracts_two_pairs(self):
        assert extract_pairs('mul(1,1)mul(2,2)') == [(1, 1), (2, 2)]

    def test_puzzle_example(self):
        example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        assert extract_pairs(example) == [(2, 4), (5, 5), (11, 8), (8, 5)]


class TestMultiplyAndSum:
    def test_puzzle_example(self):
        example = [(2, 4), (5, 5), (11, 8), (8, 5)]
        assert multiply_and_sum(example) == 161
