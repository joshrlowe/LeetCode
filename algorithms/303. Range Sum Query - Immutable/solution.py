from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0
        for num in nums:
            sum += num
            self.prefix.append(sum)
        

    def sumRange(self, left: int, right: int) -> int:
        preLeft = self.prefix[left - 1] if left > 0 else 0
        preRight = self.prefix[right]
        return preRight - preLeft