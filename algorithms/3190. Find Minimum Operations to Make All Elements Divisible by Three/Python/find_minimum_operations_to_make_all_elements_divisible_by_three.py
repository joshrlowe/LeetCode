from typing import List


def minimumOperations(nums: List[int]) -> int:
    res = 0
    for num in nums:
        if num % 3 != 0:
            res += 1
    return res
