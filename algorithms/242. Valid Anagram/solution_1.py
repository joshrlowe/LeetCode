class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        for char in freq:
            if freq[char] != 0:
                return False
        return True


def test_is_anagram():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    s1, t1 = "anagram", "nagaram"
    expected1 = True
    result1 = solution.isAnagram(s1, t1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Different lengths
    print("Test Case 2: Different lengths")
    s2, t2 = "rat", "car"
    expected2 = False
    result2 = solution.isAnagram(s2, t2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Different lengths Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Same characters but different frequencies
    print("Test Case 3: Same characters but different frequencies")
    s3, t3 = "aabbcc", "aabbc"
    expected3 = False
    result3 = solution.isAnagram(s3, t3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Same characters but different frequencies Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Empty strings
    print("Test Case 4: Empty strings")
    s4, t4 = "", ""
    expected4 = True
    result4 = solution.isAnagram(s4, t4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Empty strings Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Single character strings
    print("Test Case 5: Single character strings")
    s5, t5 = "a", "a"
    expected5 = True
    result5 = solution.isAnagram(s5, t5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Single character strings Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Single character different strings
    print("Test Case 6: Single character different strings")
    s6, t6 = "a", "b"
    expected6 = False
    result6 = solution.isAnagram(s6, t6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Single character different strings Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Longer anagram
    print("Test Case 7: Longer anagram")
    s7, t7 = "cinema", "iceman"
    expected7 = True
    result7 = solution.isAnagram(s7, t7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Longer anagram Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Non-anagram with same characters different frequencies
    print("Test Case 8: Non-anagram with same characters different frequencies")
    s8, t8 = "abc", "aabc"
    expected8 = False
    result8 = solution.isAnagram(s8, t8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Non-anagram with same characters different frequencies Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Anagram with spaces
    print("Test Case 9: Anagram with spaces")
    s9, t9 = "an a gram", "nag a ram"
    expected9 = True
    result9 = solution.isAnagram(s9, t9)
    assert (
        result9 == expected9
    ), f"Test Case 9 - Anagram with spaces Failed: Expected {expected9}, got {result9}"
    print("Passed")


if __name__ == "__main__":
    test_is_anagram()
