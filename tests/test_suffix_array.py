from src.suffix_array import SuffixArray
from tests.test_utils import sequences_equal
import pytest

def test_suffix_array():
    sa = SuffixArray("abracadabra")
    expected = ["abracadabra", "bracadabra", "racadabra", "acadabra", "cadabra", "adabra", "dabra", "abra", "bra", "ra", "a"]
    assert sequences_equal(expected, sa.suffixes)

def test_find_shortest_substr():
    sa = SuffixArray("abracadabra")
    assert sa.find_shortest_substr("abra") == "abra"
    assert sa.find_shortest_substr("ra") == "ra"
    assert sa.find_shortest_substr("raca") == "racadabra"


def test_find_longest_substr():
    sa = SuffixArray("abracadabra")
    assert sa.find_longest_substr("abra") == "abracadabra"
    assert sa.find_longest_substr("ra") == "racadabra"
    assert sa.find_longest_substr("raca") == "racadabra"

@pytest.mark.parametrize("input, expected", [
    ("abra", ['abra', 'abracadabra']), 
    ("bra", ["bra", "bracadabra"])
])
def test_find_all_substrs(input, expected):
    sa = SuffixArray("abracadabra")
    assert sequences_equal(sa.find_all_substrs(input), expected)
