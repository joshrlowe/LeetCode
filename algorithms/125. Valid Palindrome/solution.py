class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


def test_is_palindrome():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    s1 = "A man, a plan, a canal: Panama"
    expected1 = True
    result1 = solution.isPalindrome(s1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Not a palindrome
    print("Test Case 2: Not a palindrome")
    s2 = "race a car"
    expected2 = False
    result2 = solution.isPalindrome(s2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Empty string
    print("Test Case 3: Empty string")
    s3 = ""
    expected3 = True
    result3 = solution.isPalindrome(s3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single character
    print("Test Case 4: Single character")
    s4 = "a"
    expected4 = True
    result4 = solution.isPalindrome(s4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Palindrome with special characters
    print("Test Case 5: Palindrome with special characters")
    s5 = ".,"
    expected5 = True
    result5 = solution.isPalindrome(s5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Palindrome with alphanumeric characters
    print("Test Case 6: Palindrome with alphanumeric characters")
    s6 = "0P0"
    expected6 = True
    result6 = solution.isPalindrome(s6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Mixed case palindrome
    print("Test Case 7: Mixed case palindrome")
    s7 = "MadamInEdenImAdam"
    expected7 = True
    result7 = solution.isPalindrome(s7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Mixed case non-palindrome
    print("Test Case 8: Mixed case non-palindrome")
    s8 = "HelloWorld"
    expected8 = False
    result8 = solution.isPalindrome(s8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Palindrome with spaces and punctuation
    print("Test Case 9: Palindrome with spaces and punctuation")
    s9 = "No 'x' in Nixon"
    expected9 = True
    result9 = solution.isPalindrome(s9)
    assert (
        result9 == expected9
    ), f"Test Case 9 Failed: Expected {expected9}, got {result9}"
    print("Passed")


if __name__ == "__main__":
    test_is_palindrome()
