from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        min_element = min(nums)
        max_element = max(nums)

        index = 0
        for i in range(min_element, max_element + 1):
            if i in frequency:
                while frequency[i] != 0:
                    nums[index] = i
                    frequency[i] -= 1
                    index += 1

        return nums
