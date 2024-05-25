from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        last_character = "1"
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                last_character = str(bits[i]) + str(bits[i + 1])
                i += 2
            else:
                last_character = str(bits[i])
                i += 1
        return last_character == "0"


def test_is_one_bit_character():
    solution = Solution()

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    bits1 = [1, 0, 0]
    expected1 = True
    result1 = solution.isOneBitCharacter(bits1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Ends with two-bit character
    print("Test Case 2: Ends with two-bit character")
    bits2 = [1, 1, 1, 0]
    expected2 = False
    result2 = solution.isOneBitCharacter(bits2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single one-bit character
    print("Test Case 3: Single one-bit character")
    bits3 = [0]
    expected3 = True
    result3 = solution.isOneBitCharacter(bits3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single two-bit character
    print("Test Case 4: Single two-bit character")
    bits4 = [1, 0]
    expected4 = False
    result4 = solution.isOneBitCharacter(bits4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Mixed one-bit and two-bit characters
    print("Test Case 5: Mixed one-bit and two-bit characters")
    bits5 = [1, 1, 0, 0]
    expected5 = True
    result5 = solution.isOneBitCharacter(bits5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: All one-bit characters
    print("Test Case 6: All one-bit characters")
    bits6 = [0, 0, 0]
    expected6 = True
    result6 = solution.isOneBitCharacter(bits6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Complex sequence
    print("Test Case 7: Complex sequence")
    bits7 = [1, 1, 0, 1, 0, 0]
    expected7 = True
    result7 = solution.isOneBitCharacter(bits7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Another complex sequence
    print("Test Case 8: Another complex sequence")
    bits8 = [1, 0, 1, 1, 1, 0]
    expected8 = False
    result8 = solution.isOneBitCharacter(bits8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_is_one_bit_character()
