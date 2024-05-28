from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y - x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(y / x),
        }
        for token in tokens:
            if token in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operators[token](operand1, operand2))
            else:
                stack.append(int(token))
        return stack.pop()


def test_evalRPN():
    solution = Solution()

    # Test Case 1: Basic operations
    print("Test 1: Basic operations")
    tokens = ["2", "1", "+", "3", "*"]
    expected = 9
    result = solution.evalRPN(tokens)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Division and subtraction
    print("Test 2: Division and subtraction")
    tokens = ["4", "13", "5", "/", "+"]
    expected = 6
    result = solution.evalRPN(tokens)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Mixed operations
    print("Test 3: Mixed operations")
    tokens = ["10", "6", "9", "3", "/", "-", "11", "*", "+", "17", "+", "5", "+"]
    expected = 65
    result = solution.evalRPN(tokens)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Single number
    print("Test 4: Single number")
    tokens = ["42"]
    expected = 42
    result = solution.evalRPN(tokens)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Negative results
    print("Test 5: Negative results")
    tokens = ["3", "4", "-"]
    expected = -1
    result = solution.evalRPN(tokens)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Division rounding
    print("Test 6: Division rounding")
    tokens = ["7", "2", "/"]
    expected = 3
    result = solution.evalRPN(tokens)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")


if __name__ == "__main__":
    test_evalRPN()
