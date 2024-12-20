from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    def backtrack(start, cur_sum):
        if len(slate) == k and cur_sum == n:
            result.append(slate[:])
            return
        for i in range(start, 10):
            if cur_sum + i > n or len(slate) == k:
                break
            slate.append(i)
            backtrack(i + 1, cur_sum + i)
            slate.pop()

    slate, result = [], []
    backtrack(1, 0)
    return result
