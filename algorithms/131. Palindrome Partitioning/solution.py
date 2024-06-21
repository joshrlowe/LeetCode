from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        def helper(start):
            if start == len(s):
                res.append(substrings[:])
                return

            for i in range(start, len(s)):
                if self.isPalindrome(s[start : i + 1]):
                    substrings.append(s[start : i + 1])
                    helper(i + 1)
                    substrings.pop()

        res, substrings = [], []
        helper(0)
        return res


def test_partition():
    solution = Solution()

    # Test case 1: Regular case
    print("Test case 1: Regular case")
    s = "aab"
    expected = [["a", "a", "b"], ["aa", "b"]]
    result = solution.partition(s)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: Single character
    print("Test case 2: Single character")
    s = "a"
    expected = [["a"]]
    result = solution.partition(s)
    assert sorted(result) == sorted(expected), "Test case 2 failed"
    print("Passed")

    # Test case 3: Empty string
    print("Test case 3: Empty string")
    s = ""
    expected = [[]]
    result = solution.partition(s)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: All characters are the same
    print("Test case 4: All characters are the same")
    s = "aaa"
    expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    result = solution.partition(s)
    assert sorted(result) == sorted(expected), "Test case 4 failed"
    print("Passed")

    # Test case 5: No palindromic partitions
    print("Test case 5: No palindromic partitions")
    s = "abc"
    expected = [["a", "b", "c"]]
    result = solution.partition(s)
    assert sorted(result) == sorted(expected), "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_partition()
