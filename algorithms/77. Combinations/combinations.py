from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    def helper(i):
        if len(path) == k:
            result.append(path[:])
            return
        if i > n:
            return
        for j in range(i, n + 1):
            path.append(j)
            helper(j + 1)
            path.pop()

    result, path = [], []
    helper(1)
    return result
