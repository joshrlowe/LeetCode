from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def helper(partial, i):
        if i == len(nums):
            return res.append(partial[:])

        partial.append(nums[i])
        helper(partial, i + 1)
        partial.pop()
        helper(partial, i + 1)

    res, partial = [], []
    helper(partial, 0)
    return res
