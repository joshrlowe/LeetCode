from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        prefix = nums[0]
        for i in range(1, len(nums)):
            if prefix < 0:
                prefix = nums[i]
            else:
                prefix += nums[i]
            if prefix > global_sum:
                global_sum = prefix
        return global_sum