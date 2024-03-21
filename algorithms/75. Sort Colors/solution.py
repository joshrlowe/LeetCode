from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_count = [0, 0, 0]
        for num in nums:
            match(num):
                case 0:
                    color_count[0] += 1
                case 1:
                    color_count[1] += 1
                case 2:
                    color_count[2] += 1
        i = 0
        for j in range(len(color_count)):
            for _ in range(color_count[j]):
                nums[i] = j
                i += 1