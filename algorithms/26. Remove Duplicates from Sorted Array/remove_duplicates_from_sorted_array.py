from typing import List


def removeDuplicates(nums: List[int]) -> int:
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[i], nums[k] = nums[k], nums[i]
    return k + 1 if len(nums) != 0 else 0
