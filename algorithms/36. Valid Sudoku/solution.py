from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                    return False

                rows[i].add(num)
                columns[j].add(num)
                boxes[box_index].add(num)

        return True


def test_isValidSudoku():
    solution = Solution()

    # Test Case 1: Valid Sudoku board
    print("Test 1: Valid Sudoku board")
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    expected = True
    result = solution.isValidSudoku(board)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: Invalid Sudoku board with duplicate in a row
    print("Test 2: Invalid Sudoku board with duplicate in a row")
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "8"],  # Duplicate '8' in the last row
    ]
    expected = False
    result = solution.isValidSudoku(board)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Invalid Sudoku board with duplicate in a 3x3 box
    print("Test 3: Invalid Sudoku board with duplicate in a 3x3 box")
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [
            ".",
            ".",
            ".",
            ".",
            "8",
            ".",
            ".",
            "7",
            "5",
        ],  # Duplicate '5' in the bottom-left 3x3 box
    ]
    expected = False
    result = solution.isValidSudoku(board)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Valid Sudoku board with minimal numbers
    print("Test 4: Valid Sudoku board with minimal numbers")
    board = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    expected = True
    result = solution.isValidSudoku(board)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")


if __name__ == "__main__":
    test_isValidSudoku()
