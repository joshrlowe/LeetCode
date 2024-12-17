from typing import List


def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i], nums[k] = nums[k], nums[i]
            k += 1
    return k
