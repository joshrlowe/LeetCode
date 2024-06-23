from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
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


def test_exist():
    solution = Solution()

    # Test case 1: Regular case
    print("Test case 1: Regular case")
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    expected = True
    result = solution.exist(board, word)
    assert result == expected, "Test case 1 failed"
    print("Passed")

    # Test case 2: Word not present
    print("Test case 2: Word not present")
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    expected = False
    result = solution.exist(board, word)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single cell board with matching word
    print("Test case 3: Single cell board with matching word")
    board = [["A"]]
    word = "A"
    expected = True
    result = solution.exist(board, word)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Single cell board with non-matching word
    print("Test case 4: Single cell board with non-matching word")
    board = [["A"]]
    word = "B"
    expected = False
    result = solution.exist(board, word)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Word longer than board dimensions
    print("Test case 5: Word longer than board dimensions")
    board = [["A", "B"], ["C", "D"]]
    word = "ABCDAB"
    expected = False
    result = solution.exist(board, word)
    assert result == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Word that requires revisiting cells (should be False)
    print("Test case 6: Word that requires revisiting cells (should be False)")
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    expected = True
    result = solution.exist(board, word)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_exist()
