from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    def backtrack(i):
        if i >= len(nums):
            subsets.append(current[:])
            return

        current.append(nums[i])
        backtrack(i + 1)
        current.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1)

    subsets, current = [], []
    nums.sort()
    backtrack(0)
    return subsets
