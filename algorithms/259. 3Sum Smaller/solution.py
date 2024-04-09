from typing import List 


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallerSums = 0
        for i, a in enumerate(nums):
            new_target = target - a
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < new_target:
                    smallerSums += r - l
                    l += 1
                else:
                    r -= 1
        return smallerSums
                