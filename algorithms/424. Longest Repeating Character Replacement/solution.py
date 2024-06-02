class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        maxFrequency = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFrequency = max(maxFrequency, count[s[r]])

            while r - l - maxFrequency + 1 > k:
                count[s[l]] -= 1
                l += 1
                maxFrequency = max(count.values())

            res = max(res, r - l + 1)

        return res


# Test Cases
def test_characterReplacement():
    solution = Solution()

    # Test Case 1: Simple case where k is 0
    print("Test 1: Simple case where k is 0")
    s = "AABABBA"
    k = 0
    expected = 2
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Simple case where k is greater than 0
    print("Test 2: Simple case where k is greater than 0")
    s = "AABABBA"
    k = 1
    expected = 4
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: All characters are the same
    print("Test 3: All characters are the same")
    s = "AAAA"
    k = 2
    expected = 4
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: No replacement needed
    print("Test 4: No replacement needed")
    s = "ABAB"
    k = 2
    expected = 4
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Large k value
    print("Test 5: Large k value")
    s = "AABABBA"
    k = 10
    expected = 7
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Empty string
    print("Test 6: Empty string")
    s = ""
    k = 5
    expected = 0
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Single character string
    print("Test 7: Single character string")
    s = "A"
    k = 2
    expected = 1
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Mixed characters with limited replacements
    print("Test 8: Mixed characters with limited replacements")
    s = "ABAA"
    k = 1
    expected = 4
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")

    # Test Case 9: Edge case with all unique characters and no replacements
    print("Test 9: Edge case with all unique characters and no replacements")
    s = "ABCDEFG"
    k = 0
    expected = 1
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 9 Failed: expected {expected}, got {result}"
    print("Test 9 Passed")

    # Test Case 10: Edge case with all unique characters and enough replacements
    print("Test 10: Edge case with all unique characters and enough replacements")
    s = "ABCDEFG"
    k = 6
    expected = 7
    result = solution.characterReplacement(s, k)
    assert result == expected, f"Test 10 Failed: expected {expected}, got {result}"
    print("Test 10 Passed")


if __name__ == "__main__":
    test_characterReplacement()
