from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False


def test_containsNearbyDuplicate():
    solution = Solution()

    # Test Case 1: Simple case with nearby duplicates
    print("Test 1: Simple case with nearby duplicates")
    nums = [1, 2, 3, 1]
    k = 3
    expected = True
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: No duplicates
    print("Test 2: No duplicates")
    nums = [1, 2, 3, 4]
    k = 1
    expected = False
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Duplicates but not within k distance
    print("Test 3: Duplicates but not within k distance")
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    expected = False
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Edge case with k = 0
    print("Test 4: Edge case with k = 0")
    nums = [1, 2, 3, 1]
    k = 0
    expected = False
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: Edge case with k = len(nums) - 1
    print("Test 5: Edge case with k = len(nums) - 1")
    nums = [1, 2, 3, 1]
    k = 3
    expected = True
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Large array with duplicates within k distance
    print("Test 6: Large array with duplicates within k distance")
    nums = list(range(10000)) + [1]
    k = 10000
    expected = True
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Large array without duplicates
    print("Test 7: Large array without duplicates")
    nums = list(range(100000))
    k = 50000
    expected = False
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")

    # Test Case 8: Small array, k larger than array size
    print("Test 8: Small array, k larger than array size")
    nums = [1, 2, 3]
    k = 10
    expected = False
    result = solution.containsNearbyDuplicate(nums, k)
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_containsNearbyDuplicate()
