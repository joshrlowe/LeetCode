from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit, maxProfit = 0, 0
        buy = 0

        for sell in range(len(prices)):
            maxProfit = max(maxProfit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell

        return maxProfit


# Test Cases
def test_maxProfit():
    solution = Solution()

    # Test Case 1: Simple increasing prices
    print("Test 1: Simple increasing prices")
    prices = [1, 2, 3, 4, 5]
    expected = 4
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Simple decreasing prices
    print("Test 2: Simple decreasing prices")
    prices = [5, 4, 3, 2, 1]
    expected = 0
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Prices with a peak in the middle
    print("Test 3: Prices with a peak in the middle")
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Prices with no profit opportunity
    print("Test 4: Prices with no profit opportunity")
    prices = [7, 6, 4, 3, 1]
    expected = 0
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Empty prices list
    print("Test 5: Empty prices list")
    prices = []
    expected = 0
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Single day prices
    print("Test 6: Single day prices")
    prices = [5]
    expected = 0
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Multiple days with the same price
    print("Test 7: Multiple days with the same price")
    prices = [5, 5, 5, 5, 5]
    expected = 0
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Prices with profit opportunity at the end
    print("Test 8: Prices with profit opportunity at the end")
    prices = [2, 4, 1, 7]
    expected = 6
    result = solution.maxProfit(prices)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_maxProfit()
