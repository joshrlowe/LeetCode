from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0
        queue = deque()

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                output.append(nums[queue[0]])
                l += 1
            r += 1

        return output


def test_maxSlidingWindow():
    solution = Solution()

    # Test case 1: Regular case with multiple elements
    print("Test case 1: Regular case with multiple elements")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7]
    result = solution.maxSlidingWindow(nums, k)
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Single element window
    print("Test case 2: Single element window")
    nums = [1, 2, 3, 4, 5, 6]
    k = 1
    expected = [1, 2, 3, 4, 5, 6]
    result = solution.maxSlidingWindow(nums, k)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Window size equal to list size
    print("Test case 3: Window size equal to list size")
    nums = [1, 3, 5, 7, 9]
    k = 5
    expected = [9]
    result = solution.maxSlidingWindow(nums, k)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: All negative elements
    print("Test case 4: All negative elements")
    nums = [-1, -3, -6, -7, -9, -2, -5, -4]
    k = 3
    expected = [-1, -3, -6, -2, -2, -2]
    result = solution.maxSlidingWindow(nums, k)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Mixed positive and negative elements
    print("Test case 5: Mixed positive and negative elements")
    nums = [-1, 3, -1, 5, 3, 6, 7]
    k = 4
    expected = [5, 5, 6, 7]
    result = solution.maxSlidingWindow(nums, k)
    assert result == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Single element in the list
    print("Test case 6: Single element in the list")
    nums = [5]
    k = 1
    expected = [5]
    result = solution.maxSlidingWindow(nums, k)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_maxSlidingWindow()
