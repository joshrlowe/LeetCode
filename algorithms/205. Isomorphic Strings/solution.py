class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            if s[i] in s_dict and s_dict[s[i]] != t[i]:
                return False
            if t[i] in t_dict and t_dict[t[i]] != s[i]:
                return False
            s_dict[s[i]] = t[i]
            t_dict[t[i]] = s[i]
        return True


def test_is_isomorphic():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    s1, t1 = "egg", "add"
    expected1 = True
    result1 = solution.isIsomorphic(s1, t1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Not isomorphic
    print("Test Case 2: Not isomorphic")
    s2, t2 = "foo", "bar"
    expected2 = False
    result2 = solution.isIsomorphic(s2, t2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Not isomorphic Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Isomorphic with different characters
    print("Test Case 3: Isomorphic with different characters")
    s3, t3 = "paper", "title"
    expected3 = True
    result3 = solution.isIsomorphic(s3, t3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Isomorphic with different characters Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single character strings
    print("Test Case 4: Single character strings")
    s4, t4 = "a", "b"
    expected4 = True
    result4 = solution.isIsomorphic(s4, t4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Single character strings Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Strings of different lengths
    print("Test Case 5: Strings of different lengths")
    s5, t5 = "ab", "aa"
    expected5 = False
    result5 = solution.isIsomorphic(s5, t5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Strings of different lengths Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Empty strings
    print("Test Case 6: Empty strings")
    s6, t6 = "", ""
    expected6 = True
    result6 = solution.isIsomorphic(s6, t6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Empty strings Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Longer strings with isomorphic mapping
    print("Test Case 7: Longer strings with isomorphic mapping")
    s7, t7 = "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"
    expected7 = True
    result7 = solution.isIsomorphic(s7, t7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Longer strings with isomorphic mapping Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Longer strings without isomorphic mapping
    print("Test Case 8: Longer strings without isomorphic mapping")
    s8, t8 = "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyy"
    expected8 = False
    result8 = solution.isIsomorphic(s8, t8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Longer strings without isomorphic mapping Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_is_isomorphic()
