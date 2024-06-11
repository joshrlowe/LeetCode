from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


def run_test_case(test_case_num, nums, expected):
    solution = Solution()
    result = solution.findDuplicate(nums)
    assert (
        result == expected
    ), f"Test case {test_case_num} failed: expected {expected}, got {result}"
    print(f"Test case {test_case_num} - Passed")


def test_findDuplicate():
    solution = Solution()

    # Test case 1: Simple case with small array
    print("Test case 1: Simple case with small array")
    nums = [1, 3, 4, 2, 2]
    run_test_case(1, nums, 2)

    # Test case 2: Duplicate at the beginning
    print("Test case 2: Duplicate at the beginning")
    nums = [3, 1, 3, 4, 2]
    run_test_case(2, nums, 3)

    # Test case 3: Duplicate at the end
    print("Test case 3: Duplicate at the end")
    nums = [1, 4, 6, 3, 2, 5, 6]
    run_test_case(3, nums, 6)

    # Test case 4: Large array with duplicate in the middle
    print("Test case 4: Large array with duplicate in the middle")
    nums = list(range(1, 100001))
    nums.append(50000)
    run_test_case(4, nums, 50000)

    # Test case 5: Small array with minimum values
    print("Test case 5: Small array with minimum values")
    nums = [1, 1]
    run_test_case(5, nums, 1)

    # Test case 6: Random case with a mix of numbers
    print("Test case 6: Random case with a mix of numbers")
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    run_test_case(6, nums, 9)

    # Test case 7: Duplicate at the second position
    print("Test case 7: Duplicate at the second position")
    nums = [1, 3, 4, 2, 5, 3]
    run_test_case(7, nums, 3)


if __name__ == "__main__":
    test_findDuplicate()
