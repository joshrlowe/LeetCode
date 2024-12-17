from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def helper(i):
        if i == len(nums):
            return [[]]

        res = []
        perms = helper(i + 1)
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p[:]
                pCopy.insert(j, nums[i])
                res.append(pCopy)
        return res

    return helper(0)
