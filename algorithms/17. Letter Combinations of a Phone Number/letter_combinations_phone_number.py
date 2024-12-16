from typing import List


def letterCombinations(digits: str) -> List[str]:
    combinations = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def helper(i):
        if i == len(digits):
            result.append("".join(partial_solution))
            return
        for j in combinations[digits[i]]:
            partial_solution.append(j)
            helper(i + 1)
            partial_solution.pop()

    if len(digits) == 0:
        return []

    result, partial_solution = [], []
    helper(0)
    return result
