import pytest  # type: ignore
from Python.group_anagrams_solution_1 import groupAnagrams as group_anagrams_1
from Python.group_anagrams_solution_2 import groupAnagrams as group_anagrams_2
from typing import List


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        (
            ["abc", "bca", "cab", "a", "b", "c"],
            [["abc", "bca", "cab"], ["a"], ["b"], ["c"]],
        ),
        (
            ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "ant", "tna"],
            [["eat", "tea", "ate"], ["tan", "nat", "ant", "tna"], ["bat", "tab"]],
        ),
        (["a", "a", "a"], [["a", "a", "a"]]),
    ],
)
def test_group_anagrams(strs: List[str], expected: List[List[str]]):
    result_1 = sorted(group_anagrams_1(strs))
    result_2 = sorted(group_anagrams_2(strs))
    expected.sort()
    assert (
        result_1 == expected
    ), f"strs = {strs}, expected = {expected}, result_1 = {result_1}"
    assert (
        result_2 == expected
    ), f"strs = {strs}, expected = {expected}, result_2 = {result_2}"
