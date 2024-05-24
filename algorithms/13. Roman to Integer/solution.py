class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_sum = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                roman_sum += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                roman_sum += values[s[i]]
                i += 1
        return roman_sum


def test_roman_to_int():
    solution = Solution()

    # Test case 1: Basic Roman numeral
    print("Test case 1: Basic Roman numeral")
    s = "III"
    assert solution.romanToInt(s) == 3  # III = 3
    print("Passed")

    # Test case 2: Subtraction rule
    print("Test case 2: Subtraction rule")
    s = "IV"
    assert solution.romanToInt(s) == 4  # IV = 4
    print("Passed")

    # Test case 3: Combination of addition and subtraction
    print("Test case 3: Combination of addition and subtraction")
    s = "IX"
    assert solution.romanToInt(s) == 9  # IX = 9
    print("Passed")

    # Test case 4: Larger Roman numerals
    print("Test case 4: Larger Roman numerals")
    s = "LVIII"
    assert solution.romanToInt(s) == 58  # L = 50, V = 5, III = 3
    print("Passed")

    # Test case 5: Complex combination
    print("Test case 5: Complex combination")
    s = "MCMXCIV"
    assert solution.romanToInt(s) == 1994  # M = 1000, CM = 900, XC = 90, IV = 4
    print("Passed")

    # Test case 6: Single character
    print("Test case 6: Single character")
    s = "M"
    assert solution.romanToInt(s) == 1000  # M = 1000
    print("Passed")

    # Test case 7: Sequential characters with no subtraction
    print("Test case 7: Sequential characters with no subtraction")
    s = "VI"
    assert solution.romanToInt(s) == 6  # V = 5, I = 1
    print("Passed")

    # Test case 8: Repeating characters
    print("Test case 8: Repeating characters")
    s = "XX"
    assert solution.romanToInt(s) == 20  # X = 10, X = 10
    print("Passed")

    # Test case 9: Complex subtraction cases
    print("Test case 9: Complex subtraction cases")
    s = "XLIX"
    assert solution.romanToInt(s) == 49  # XL = 40, IX = 9
    print("Passed")


if __name__ == "__main__":
    test_roman_to_int()
