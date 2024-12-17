from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(i, current):
        if current == target:
            result.append(path.copy())
            return
        if i >= len(candidates) or current > target:
            return
        path.append(candidates[i])
        backtrack(i, current + candidates[i])
        path.pop()
        backtrack(i + 1, current)

    result, path = [], []
    backtrack(0, 0)
    return result
