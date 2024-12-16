from typing import List


def generateParenthesis(n: int) -> List[str]:
    def backtrack(opened, closed):
        if len(slate) == 2 * n:
            result.append("".join(slate))

        if opened < n:
            slate.append("(")
            backtrack(opened + 1, closed)
            slate.pop()

        if closed < opened:
            slate.append(")")
            backtrack(opened, closed + 1)
            slate.pop()

    slate, result = [], []
    backtrack(0, 0)
    return result
