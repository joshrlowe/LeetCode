from typing import List


def orArray(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i - 1] | nums[i]
    return nums[1:]
