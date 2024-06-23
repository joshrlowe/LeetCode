"""
Top-Down (Memoization) Solution
O(n) Time Complexity
O(n) Space Complexity
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def memoization(i):
            if i <= 2:
                return i
            if i in cache:
                return cache[i]
            cache[i] = memoization(i - 1) + memoization(i - 2)
            return cache[i]

        return memoization(n)


def test_climbStairs():
    solution = Solution()

    # Test case 1: Base case n = 1
    print("Test case 1: Base case n = 1")
    n = 1
    expected = 1
    result = solution.climbStairs(n)
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Base case n = 2
    print("Test case 2: Base case n = 2")
    n = 2
    expected = 2
    result = solution.climbStairs(n)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Regular case n = 3
    print("Test case 3: Regular case n = 3")
    n = 3
    expected = 3
    result = solution.climbStairs(n)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Regular case n = 4
    print("Test case 4: Regular case n = 4")
    n = 4
    expected = 5
    result = solution.climbStairs(n)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Regular case n = 5
    print("Test case 5: Regular case n = 5")
    n = 5
    expected = 8
    result = solution.climbStairs(n)
    assert result == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Larger case n = 10
    print("Test case 6: Larger case n = 10")
    n = 10
    expected = 89
    result = solution.climbStairs(n)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_climbStairs()
