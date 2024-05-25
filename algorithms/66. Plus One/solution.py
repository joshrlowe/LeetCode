from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i > -1:
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
            else:
                break
        if i == -1:
            digits[0] = 1
            digits.append(0)
        return digits


def test_plus_one():
    solution = Solution()

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    digits1 = [1, 2, 3]
    expected1 = [1, 2, 4]
    result1 = solution.plusOne(digits1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Increment with carry
    print("Test Case 2: Increment with carry")
    digits2 = [1, 2, 9]
    expected2 = [1, 3, 0]
    result2 = solution.plusOne(digits2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Increment causing new digit
    print("Test Case 3: Increment causing new digit")
    digits3 = [9, 9, 9]
    expected3 = [1, 0, 0, 0]
    result3 = solution.plusOne(digits3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single digit
    print("Test Case 4: Single digit")
    digits4 = [0]
    expected4 = [1]
    result4 = solution.plusOne(digits4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Large number with multiple carries
    print("Test Case 5: Large number with multiple carries")
    digits5 = [2, 9, 9, 9]
    expected5 = [3, 0, 0, 0]
    result5 = solution.plusOne(digits5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Single 9 digit
    print("Test Case 6: Single 9 digit")
    digits6 = [9]
    expected6 = [1, 0]
    result6 = solution.plusOne(digits6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Multiple zeros
    print("Test Case 7: Multiple zeros")
    digits7 = [0, 0, 0]
    expected7 = [0, 0, 1]
    result7 = solution.plusOne(digits7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_plus_one()
