class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        temp = x
        while temp != 0:
            reverse *= 10
            reverse += temp % 10
            temp //= 10
        return reverse == x


def test_is_palindrome():
    solution = Solution()

    # Test case 1: Positive palindrome number
    print("Test case 1: Positive palindrome number")
    x = 121
    assert solution.isPalindrome(x) == True  # 121 is a palindrome
    print("Passed")

    # Test case 2: Negative number
    print("Test case 2: Negative number")
    x = -121
    assert solution.isPalindrome(x) == False  # Negative numbers are not palindromes
    print("Passed")

    # Test case 3: Number with trailing zeros
    print("Test case 3: Number with trailing zeros")
    x = 10
    assert solution.isPalindrome(x) == False  # 10 is not a palindrome
    print("Passed")

    # Test case 4: Single digit number
    print("Test case 4: Single digit number")
    x = 7
    assert solution.isPalindrome(x) == True  # Single digit numbers are palindromes
    print("Passed")

    # Test case 5: Large palindrome number
    print("Test case 5: Large palindrome number")
    x = 123454321
    assert solution.isPalindrome(x) == True  # 123454321 is a palindrome
    print("Passed")

    # Test case 6: Large non-palindrome number
    print("Test case 6: Large non-palindrome number")
    x = 123456789
    assert solution.isPalindrome(x) == False  # 123456789 is not a palindrome
    print("Passed")

    # Test case 7: Zero
    print("Test case 7: Zero")
    x = 0
    assert solution.isPalindrome(x) == True  # 0 is a palindrome
    print("Passed")


if __name__ == "__main__":
    test_is_palindrome()
