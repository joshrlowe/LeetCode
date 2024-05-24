class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        reversed = 0
        while x > 0:
            reversed += x % 10
            x -= x % 10
            x /= 10
            reversed *= 10
        x = -1 * int(reversed // 10) if negative else int(reversed // 10)
        return x if x.bit_length() < 32 else 0


def test_reverse_integer():
    solution = Solution()

    # Test case 1: Basic positive number
    print("Test case 1: Basic positive number")
    x = 123
    assert solution.reverse(x) == 321  # Reversed: 321
    print("Passed")

    # Test case 2: Basic negative number
    print("Test case 2: Basic negative number")
    x = -123
    assert solution.reverse(x) == -321  # Reversed: -321
    print("Passed")

    # Test case 3: Number with trailing zeros
    print("Test case 3: Number with trailing zeros")
    x = 120
    assert solution.reverse(x) == 21  # Reversed: 021 -> 21
    print("Passed")

    # Test case 4: Single digit number
    print("Test case 4: Single digit number")
    x = 5
    assert solution.reverse(x) == 5  # Reversed: 5
    print("Passed")

    # Test case 5: Zero
    print("Test case 5: Zero")
    x = 0
    assert solution.reverse(x) == 0  # Reversed: 0
    print("Passed")

    # Test case 6: Large positive number
    print("Test case 6: Large positive number")
    x = 1534236469
    assert solution.reverse(x) == 0  # Reversed number exceeds 32-bit integer range
    print("Passed")

    # Test case 7: Large negative number
    print("Test case 7: Large negative number")
    x = -1534236469
    assert solution.reverse(x) == 0  # Reversed number exceeds 32-bit integer range
    print("Passed")


if __name__ == "__main__":
    test_reverse_integer()
