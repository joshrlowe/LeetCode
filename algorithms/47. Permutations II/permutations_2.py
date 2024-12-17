from collections import Counter
from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    def dfs():
        if len(perm) == len(nums):
            result.append(perm[:])
            return
        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1
                dfs()
                count[n] += 1
                perm.pop()

    result, perm = [], []
    count = Counter(nums)
    dfs()
    return result
