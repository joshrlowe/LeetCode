class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-0.5 + (0.25 + 2 * n) ** 0.5)


def test_arrange_coins():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    n1 = 5
    expected1 = 2
    result1 = solution.arrangeCoins(n1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: Exact number of coins to form a full row
    print("Test Case 2: Exact number of coins to form a full row")
    n2 = 6
    expected2 = 3
    result2 = solution.arrangeCoins(n2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - Exact number of coins to form a full row Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Larger number of coins
    print("Test Case 3: Larger number of coins")
    n3 = 8
    expected3 = 3
    result3 = solution.arrangeCoins(n3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Larger number of coins Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Zero coins
    print("Test Case 4: Zero coins")
    n4 = 0
    expected4 = 0
    result4 = solution.arrangeCoins(n4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Zero coins Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: One coin
    print("Test Case 5: One coin")
    n5 = 1
    expected5 = 1
    result5 = solution.arrangeCoins(n5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - One coin Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Large number of coins
    print("Test Case 6: Large number of coins")
    n6 = 1000000000
    expected6 = 44720
    result6 = solution.arrangeCoins(n6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Large number of coins Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Another small number of coins
    print("Test Case 7: Another small number of coins")
    n7 = 3
    expected7 = 2
    result7 = solution.arrangeCoins(n7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Another small number of coins Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Perfect square number of coins
    print("Test Case 8: Perfect square number of coins")
    n8 = 36
    expected8 = 8
    result8 = solution.arrangeCoins(n8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Perfect square number of coins Failed: Expected {expected8}, got {result8}"
    print("Passed")

    # Test Case 9: One less than a perfect square
    print("Test Case 9: One less than a perfect square")
    n9 = 35
    expected9 = 7
    result9 = solution.arrangeCoins(n9)
    assert (
        result9 == expected9
    ), f"Test Case 9 - One less than a perfect square Failed: Expected {expected9}, got {result9}"
    print("Passed")

    # Test Case 10: One more than a perfect square
    print("Test Case 10: One more than a perfect square")
    n10 = 37
    expected10 = 8
    result10 = solution.arrangeCoins(n10)
    assert (
        result10 == expected10
    ), f"Test Case 10 - One more than a perfect square Failed: Expected {expected10}, got {result10}"
    print("Passed")


if __name__ == "__main__":
    test_arrange_coins()
