def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if not isBadVersion(mid):
                low = mid + 1
            elif isBadVersion(mid) and (mid == 0 or isBadVersion(mid - 1) == True):
                high = mid - 1
            else:
                return mid


def test_firstBadVersion():
    solution = Solution()

    # Test Case 1: Bad version in the middle
    global bad
    print("Test 1: Bad version in the middle")
    bad = 500
    n = 1000
    expected = 500
    result = solution.firstBadVersion(n)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Bad version is the first version
    print("Test 2: Bad version is the first version")
    bad = 1
    n = 1000
    expected = 1
    result = solution.firstBadVersion(n)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Bad version is the last version
    print("Test 3: Bad version is the last version")
    bad = 1000
    n = 1000
    expected = 1000
    result = solution.firstBadVersion(n)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Single version, which is bad
    print("Test 4: Single version, which is bad")
    bad = 1
    n = 1
    expected = 1
    result = solution.firstBadVersion(n)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Large number of versions with bad version in the middle
    print("Test 5: Large number of versions with bad version in the middle")
    bad = 2**30
    n = 2**31 - 1
    expected = 2**30
    result = solution.firstBadVersion(n)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")


if __name__ == "__main__":
    test_firstBadVersion()
