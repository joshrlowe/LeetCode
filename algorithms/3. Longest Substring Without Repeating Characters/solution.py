class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        maxLength, l = 0, 0
        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength


def test_length_of_longest_substring():
    solution = Solution()

    # Test case 1: Basic case with no repeating characters
    print("Test case 1: Basic case with no repeating characters")
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3  # "abc" is the longest substring
    print("Passed")

    # Test case 2: All unique characters
    print("Test case 2: All unique characters")
    s = "abcdef"
    assert (
        solution.lengthOfLongestSubstring(s) == 6
    )  # "abcdef" is the longest substring
    print("Passed")

    # Test case 3: All characters are the same
    print("Test case 3: All characters are the same")
    s = "aaaaaa"
    assert solution.lengthOfLongestSubstring(s) == 1  # "a" is the longest substring
    print("Passed")

    # Test case 4: Empty string
    print("Test case 4: Empty string")
    s = ""
    assert solution.lengthOfLongestSubstring(s) == 0  # The longest substring is ""
    print("Passed")

    # Test case 5: String with special characters
    print("Test case 5: String with special characters")
    s = "a!@#a!@#"
    assert solution.lengthOfLongestSubstring(s) == 4  # "!@#a" is the longest substring
    print("Passed")

    # Test case 6: String with spaces
    print("Test case 6: String with spaces")
    s = "a b c a b c"
    assert solution.lengthOfLongestSubstring(s) == 3  # "a b c" is the longest substring
    print("Passed")

    # Test case 7: Mixed case sensitivity
    print("Test case 7: Mixed case sensitivity")
    s = "aAaA"
    assert solution.lengthOfLongestSubstring(s) == 2  # "aA" is the longest substring
    print("Passed")

    # Test case 8: Long string with no repeating characters
    print("Test case 8: Long string with no repeating characters")
    s = "abcdefghijklmnopqrstuvwxyz"
    assert (
        solution.lengthOfLongestSubstring(s) == 26
    )  # "abcdefghijklmnopqrstuvwxyz" is the longest substring
    print("Passed")

    # Test case 9: String with digits
    print("Test case 9: String with digits")
    s = "a1b2c3d4"
    assert (
        solution.lengthOfLongestSubstring(s) == 8
    )  # "a1b2c3d4" is the longest substring
    print("Passed")

    # Test case 10: Long string with repeating pattern
    print("Test case 10: Long string with repeating pattern")
    s = "abcabcabcabcabcabcabcabcabcabc"
    assert solution.lengthOfLongestSubstring(s) == 3  # "abc" is the longest substring
    print("Passed")


if __name__ == "__main__":
    test_length_of_longest_substring()
