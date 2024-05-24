class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_parentheses = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in closing_parentheses:
                if stack and stack[-1] == closing_parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


def test_is_valid():
    solution = Solution()

    # Test case 1: Basic valid parentheses
    print("Test case 1: Basic valid parentheses")
    s = "()"
    assert solution.isValid(s) == True  # Valid
    print("Passed")

    # Test case 2: Mixed types valid
    print("Test case 2: Mixed types valid")
    s = "()[]{}"
    assert solution.isValid(s) == True  # Valid
    print("Passed")

    # Test case 3: Nested valid parentheses
    print("Test case 3: Nested valid parentheses")
    s = "({[]})"
    assert solution.isValid(s) == True  # Valid
    print("Passed")

    # Test case 4: Single type invalid
    print("Test case 4: Single type invalid")
    s = "(]"
    assert solution.isValid(s) == False  # Invalid
    print("Passed")

    # Test case 5: Unmatched opening parenthesis
    print("Test case 5: Unmatched opening parenthesis")
    s = "([)"
    assert solution.isValid(s) == False  # Invalid
    print("Passed")

    # Test case 6: Empty string
    print("Test case 6: Empty string")
    s = ""
    assert solution.isValid(s) == True  # Valid
    print("Passed")

    # Test case 7: Long valid string
    print("Test case 7: Long valid string")
    s = "(((()))){{{{[]}}}}"
    assert solution.isValid(s) == True  # Valid
    print("Passed")

    # Test case 8: Long invalid string
    print("Test case 8: Long invalid string")
    s = "(((())){{{{[]}}}"
    assert solution.isValid(s) == False  # Invalid
    print("Passed")

    # Test case 9: Single type repeated
    print("Test case 9: Single type repeated")
    s = "((()))"
    assert solution.isValid(s) == True  # Valid
    print("Passed")

    # Test case 10: Only closing brackets
    print("Test case 10: Only closing brackets")
    s = "}}}}"
    assert solution.isValid(s) == False  # Invalid
    print("Passed")


if __name__ == "__main__":
    test_is_valid()
