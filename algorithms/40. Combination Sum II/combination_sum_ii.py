from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    def helper(start, curSum):
        if curSum == target:
            result.append(path.copy())
            return
        if curSum > target:
            return
        for i in range(start, len(candidates)):
            if i != start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            helper(i + 1, curSum + candidates[i])
            path.pop()

    candidates.sort()
    result, path = [], []
    helper(0, 0)
    return result
