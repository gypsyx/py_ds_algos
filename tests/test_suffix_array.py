from src.suffix_array import SuffixArray
from tests.test_utils import sequences_equal
import pytest

def test_suffix_array_construction():
    sa = SuffixArray("abracadabra")
    expected = [
        ("abracadabra", 0), 
        ("bracadabra", 1), 
        ("racadabra", 2), 
        ("acadabra", 3), 
        ("cadabra", 4), 
        ("adabra", 5), 
        ("dabra", 6), 
        ("abra", 7), 
        ("bra", 8), 
        ("ra", 9), 
        ("a", 10)
    ]
    assert sequences_equal(expected, sa.suffixes)

def test_search():
    sa = SuffixArray("abracadabra")
    assert sa.search("abra") == (1, 7)
    assert sa.search("ra") == (9, 9)
    assert sa.search("raca") == (-1, -1)

def test_find_shortest_substr():
    sa = SuffixArray("abracadabra")
    assert sa.find_shortest_substr("abra") == 7
    assert sa.find_shortest_substr("ra") == 9
    assert sa.find_shortest_substr("raca") == -1


# def test_find_longest_substr():
#     sa = SuffixArray("abracadabra")
#     assert sa.find_longest_substr("abra") == "abracadabra"
#     assert sa.find_longest_substr("ra") == "racadabra"
#     assert sa.find_longest_substr("raca") == "racadabra"


# @pytest.mark.parametrize("input, expected", [
#     ("abra", ['abra', 'abracadabra']), 
#     ("bra", ["bra", "bracadabra"])
# ])
# def test_find_all_substrs(input, expected):
#     sa = SuffixArray("abracadabra")
#     assert sequences_equal(sa.find_all_substrs(input), expected)
