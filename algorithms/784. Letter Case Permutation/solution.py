from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def helper(slate, i):
            if len(s) == i:
                result.append(slate)
                return
            if s[i].isalpha():
                helper(slate + s[i].lower(), i + 1)
                helper(slate + s[i].upper(), i + 1)
            else:
                helper(slate + s[i], i + 1)

        result = []
        helper("", 0)
        return result


def test_letter_case_permutation():
    solution = Solution()

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    s1 = "a1b2"
    expected1 = ["a1b2", "a1B2", "A1b2", "A1B2"]
    result1 = solution.letterCasePermutation(s1)
    assert sorted(result1) == sorted(
        expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: All letters
    print("Test Case 2: All letters")
    s2 = "3z4"
    expected2 = ["3z4", "3Z4"]
    result2 = solution.letterCasePermutation(s2)
    assert sorted(result2) == sorted(
        expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single character
    print("Test Case 3: Single character")
    s3 = "a"
    expected3 = ["a", "A"]
    result3 = solution.letterCasePermutation(s3)
    assert sorted(result3) == sorted(
        expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single digit
    print("Test Case 4: Single digit")
    s4 = "1"
    expected4 = ["1"]
    result4 = solution.letterCasePermutation(s4)
    assert sorted(result4) == sorted(
        expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Mixed letters and digits
    print("Test Case 5: Mixed letters and digits")
    s5 = "a1"
    expected5 = ["a1", "A1"]
    result5 = solution.letterCasePermutation(s5)
    assert sorted(result5) == sorted(
        expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Upper case letters
    print("Test Case 6: Upper case letters")
    s6 = "A1B2"
    expected6 = ["a1b2", "a1B2", "A1b2", "A1B2"]
    result6 = solution.letterCasePermutation(s6)
    assert sorted(result6) == sorted(
        expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: No letters
    print("Test Case 7: No letters")
    s7 = "12345"
    expected7 = ["12345"]
    result7 = solution.letterCasePermutation(s7)
    assert sorted(result7) == sorted(
        expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Empty string
    print("Test Case 8: Empty string")
    s8 = ""
    expected8 = [""]
    result8 = solution.letterCasePermutation(s8)
    assert sorted(result8) == sorted(
        expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: Complex case with mixed letters and digits
    print("Test Case 9: Complex case with mixed letters and digits")
    s9 = "a1b2c3"
    expected9 = [
        "a1b2c3",
        "a1b2C3",
        "a1B2c3",
        "a1B2C3",
        "A1b2c3",
        "A1b2C3",
        "A1B2c3",
        "A1B2C3",
    ]
    result9 = solution.letterCasePermutation(s9)
    assert sorted(result9) == sorted(
        expected9
    ), f"Test Case 9 Failed: Expected {expected9}, got {result9}"
    print("Passed")

    # Test Case 10: All uppercase letters
    print("Test Case 10: All uppercase letters")
    s10 = "XYZ"
    expected10 = ["xyz", "xyZ", "xYz", "xYZ", "Xyz", "XyZ", "XYz", "XYZ"]
    result10 = solution.letterCasePermutation(s10)
    assert sorted(result10) == sorted(
        expected10
    ), f"Test Case 10 Failed: Expected {expected10}, got {result10}"
    print("Passed")


if __name__ == "__main__":
    test_letter_case_permutation()
