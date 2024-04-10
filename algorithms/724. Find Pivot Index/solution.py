from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        partialSum = 0
        for i in range(len(nums)):
            partialSum += nums[i]
            if partialSum - nums[i] == totalSum - partialSum:
                return i
        return -1