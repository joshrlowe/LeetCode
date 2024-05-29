from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        stack = []
        res = []
        backtrack(0, 0)
        return res


def test_generateParenthesis():
    solution = Solution()

    # Test Case 1: n = 1
    print("Test 1: n = 1")
    n = 1
    expected = ["()"]
    result = solution.generateParenthesis(n)
    assert sorted(result) == sorted(
        expected
    ), f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: n = 2
    print("Test 2: n = 2")
    n = 2
    expected = ["(())", "()()"]
    result = solution.generateParenthesis(n)
    assert sorted(result) == sorted(
        expected
    ), f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: n = 3
    print("Test 3: n = 3")
    n = 3
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result = solution.generateParenthesis(n)
    assert sorted(result) == sorted(
        expected
    ), f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: n = 0 (edge case)
    print("Test 4: n = 0")
    n = 0
    expected = [""]
    result = solution.generateParenthesis(n)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: n = 4
    print("Test 5: n = 4")
    n = 4
    expected = [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    ]
    result = solution.generateParenthesis(n)
    assert sorted(result) == sorted(
        expected
    ), f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")


if __name__ == "__main__":
    test_generateParenthesis()
