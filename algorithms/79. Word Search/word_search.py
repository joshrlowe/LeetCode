from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def backtrack(nxt, i, j):
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or board[i][j] != word[nxt]
        ):
            return False
        if nxt == len(word) - 1:
            return True

        temp, board[i][j] = board[i][j], "."
        found = (
            backtrack(nxt + 1, i + 1, j)
            or backtrack(nxt + 1, i, j + 1)
            or backtrack(nxt + 1, i - 1, j)
            or backtrack(nxt + 1, i, j - 1)
        )
        board[i][j] = temp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(0, i, j):
                return True

    return False
