from typing import List


def isValid(nxt: int, slate: List[int]) -> bool:
    for i in range(len(slate)):
        if slate[i] == nxt or abs(slate[i] - nxt) == abs(len(slate) - i):
            return False
    return True


def totalNQueens(n: int) -> int:
    def backtrack(row, start):
        nonlocal res
        if row == n:
            res += 1
            return

        for i in range(start, n):
            if isValid(choices[i], choices[:start]):
                choices[start], choices[i] = choices[i], choices[start]
                backtrack(row + 1, start + 1)
                choices[start], choices[i] = choices[i], choices[start]

    choices = list(range(n))
    res = 0
    backtrack(0, 0)
    return res
