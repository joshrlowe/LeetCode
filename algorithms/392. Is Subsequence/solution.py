class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False


def test_is_subsequence():
    solution = Solution()

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    s1, t1 = "abc", "ahbgdc"
    expected1 = True
    result1 = solution.isSubsequence(s1, t1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Not a subsequence
    print("Test Case 2: Not a subsequence")
    s2, t2 = "axc", "ahbgdc"
    expected2 = False
    result2 = solution.isSubsequence(s2, t2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Empty string s
    print("Test Case 3: Empty string s")
    s3, t3 = "", "ahbgdc"
    expected3 = True
    result3 = solution.isSubsequence(s3, t3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Empty string t
    print("Test Case 4: Empty string t")
    s4, t4 = "abc", ""
    expected4 = False
    result4 = solution.isSubsequence(s4, t4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Both strings empty
    print("Test Case 5: Both strings empty")
    s5, t5 = "", ""
    expected5 = True
    result5 = solution.isSubsequence(s5, t5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: s is longer than t
    print("Test Case 6: s is longer than t")
    s6, t6 = "abc", "a"
    expected6 = False
    result6 = solution.isSubsequence(s6, t6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Characters not in order
    print("Test Case 7: Characters not in order")
    s7, t7 = "acb", "ahbgdc"
    expected7 = False
    result7 = solution.isSubsequence(s7, t7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Single character match
    print("Test Case 8: Single character match")
    s8, t8 = "a", "a"
    expected8 = True
    result8 = solution.isSubsequence(s8, t8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Single character no match
    print("Test Case 9: Single character no match")
    s9, t9 = "a", "b"
    expected9 = False
    result9 = solution.isSubsequence(s9, t9)
    assert (
        result9 == expected9
    ), f"Test Case 9 Failed: Expected {expected9}, got {result9}"
    print("Passed")

    # Test Case 10: s is a prefix of t
    print("Test Case 10: s is a prefix of t")
    s10, t10 = "abc", "abcdef"
    expected10 = True
    result10 = solution.isSubsequence(s10, t10)
    assert (
        result10 == expected10
    ), f"Test Case 10 Failed: Expected {expected10}, got {result10}"
    print("Passed")

    # Test Case 11: s is a suffix of t
    print("Test Case 11: s is a suffix of t")
    s11, t11 = "def", "abcdef"
    expected11 = True
    result11 = solution.isSubsequence(s11, t11)
    assert (
        result11 == expected11
    ), f"Test Case 11 Failed: Expected {expected11}, got {result11}"
    print("Passed")


if __name__ == "__main__":
    test_is_subsequence()
