"""
Bottom-Up (Tabulation) Solution
O(n) Time Complexity
O(1) Space Complexity
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0, 1]
        i = 2
        while i <= n:
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
            i += 1
        return dp[1]


def test_fib():
    solution = Solution()

    # Test case 1: Base case n = 0
    print("Test case 1: Base case n = 0")
    n = 0
    expected = 0
    result = solution.fib(n)
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Base case n = 1
    print("Test case 2: Base case n = 1")
    n = 1
    expected = 1
    result = solution.fib(n)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Regular case n = 2
    print("Test case 3: Regular case n = 2")
    n = 2
    expected = 1
    result = solution.fib(n)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Regular case n = 3
    print("Test case 4: Regular case n = 3")
    n = 3
    expected = 2
    result = solution.fib(n)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Regular case n = 10
    print("Test case 5: Regular case n = 10")
    n = 10
    expected = 55
    result = solution.fib(n)
    assert result == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Regular case n = 20
    print("Test case 6: Regular case n = 20")
    n = 20
    expected = 6765
    result = solution.fib(n)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_fib()
