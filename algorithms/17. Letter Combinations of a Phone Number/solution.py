from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(i):
            if i == len(digits):
                result.append("".join(partial_solution))
                return
            for j in combinations[digits[i]]:
                partial_solution.append(j)
                helper(i + 1)
                partial_solution.pop()

        if len(digits) == 0:
            return []

        result, partial_solution = [], []
        helper(0)
        return result


def test_letter_combinations():
    solution = Solution()

    # Test case 1: Basic case with two digits
    print("Test case 1: Basic case with two digits")
    digits = "23"
    print(expected)
    print(result)
    assert sorted(result) == sorted(expected)  # Sort results for comparison
    print("Passed")

    # Test case 2: Single digit
    print("Test case 2: Single digit")
    digits = "2"
    expected = ["a", "b", "c"]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    print("Passed")

    # Test case 3: Empty input
    print("Test case 3: Empty input")
    digits = ""
    expected = []
    result = solution.letterCombinations(digits)
    assert result == expected
    print("Passed")

    # Test case 4: Digits with 4 letters
    print("Test case 4: Digits with 4 letters")
    digits = "79"
    expected = [
        "pw",
        "px",
        "py",
        "pz",
        "qw",
        "qx",
        "qy",
        "qz",
        "rw",
        "rx",
        "ry",
        "rz",
        "sw",
        "sx",
        "sy",
        "sz",
    ]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    print("Passed")

    # Test case 5: Multiple digits
    print("Test case 5: Multiple digits")
    digits = "234"
    expected = [
        "adg",
        "adh",
        "adi",
        "aeg",
        "aeh",
        "aei",
        "afg",
        "afh",
        "afi",
        "bdg",
        "bdh",
        "bdi",
        "beg",
        "beh",
        "bei",
        "bfg",
        "bfh",
        "bfi",
        "cdg",
        "cdh",
        "cdi",
        "ceg",
        "ceh",
        "cei",
        "cfg",
        "cfh",
        "cfi",
    ]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    print("Passed")

    # Test case 6: Digits leading to large output
    print("Test case 6: Digits leading to large output")
    digits = "2345"
    # We don't manually list the expected results because they are too many,
    # but we know the length should be 3^4 = 81 combinations
    result = solution.letterCombinations(digits)
    assert len(result) == 81
    print("Passed")


if __name__ == "__main__":
    test_letter_combinations()
