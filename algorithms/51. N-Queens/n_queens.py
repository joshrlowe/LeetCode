from typing import List


def construct_board(slate: List[int]) -> List[List[str]]:
    board = [["." for _ in range(len(slate))] for _ in range(len(slate))]
    for i in range(len(slate)):
        board[i][slate[i]] = "Q"
        board[i] = "".join(board[i])
    return board


def is_valid(c: int, slate: List[int]) -> bool:
    for i in range(len(slate)):
        if slate[i] == c or abs(slate[i] - c) == abs(len(slate) - i):
            return False
    return True


def solveNQueens(n: int) -> List[List[str]]:
    def helper(row, start):
        if row == n:
            result.append(construct_board(arr))
            return

        for i in range(start, n):
            if is_valid(arr[i], arr[:start]):
                arr[start], arr[i] = arr[i], arr[start]
                helper(row + 1, start + 1)
                arr[start], arr[i] = arr[i], arr[start]

    arr = list(range(n))
    result = []
    helper(0, 0)
    return result
