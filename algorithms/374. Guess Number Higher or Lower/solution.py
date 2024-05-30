def guess(num: int) -> int:
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if guess(mid) > 0:
                low = mid + 1
            elif guess(mid) < 0:
                high = mid - 1
            else:
                return mid


def test_guessNumber():
    solution = Solution()

    # Test Case 1: Middle of the range
    global pick
    print("Test 1: Middle of the range")
    pick = 500
    n = 1000
    expected = 500
    result = solution.guessNumber(n)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Lower end of the range
    print("Test 2: Lower end of the range")
    pick = 1
    n = 1000
    expected = 1
    result = solution.guessNumber(n)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Upper end of the range
    print("Test 3: Upper end of the range")
    pick = 1000
    n = 1000
    expected = 1000
    result = solution.guessNumber(n)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Single element range
    print("Test 4: Single element range")
    pick = 1
    n = 1
    expected = 1
    result = solution.guessNumber(n)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Large range, pick in the middle
    print("Test 5: Large range, pick in the middle")
    pick = 2**30
    n = 2**31 - 1
    expected = 2**30
    result = solution.guessNumber(n)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")


if __name__ == "__main__":
    test_guessNumber()
