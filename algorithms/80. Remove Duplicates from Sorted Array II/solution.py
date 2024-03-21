from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k - 2 < 0 or nums[i] != nums[k - 2]:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return k