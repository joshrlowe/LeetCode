from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    perms = [[]]

    for n in nums:
        nextPerms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p[:]
                pCopy.insert(i, n)
                nextPerms.append(pCopy)
        perms = nextPerms
    return perms
