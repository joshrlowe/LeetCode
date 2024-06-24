from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == len(board)
                or c == len(board[0])
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return False
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")

        return list(res)


def test_findWords():
    solution = Solution()

    # Test case 1: Regular case with multiple words
    print("Test case 1: Regular case with multiple words")
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    expected = ["oath", "eat"]
    result = solution.findWords(board, words)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: Single word found
    print("Test case 2: Single word found")
    board = [["a", "b"], ["c", "d"]]
    words = ["abcd"]
    expected = []
    result = solution.findWords(board, words)
    assert sorted(result) == sorted(expected), "Test case 2 failed"
    print("Passed")

    # Test case 3: All words found
    print("Test case 3: All words found")
    board = [["a", "b"], ["c", "d"]]
    words = ["ab", "abc", "abd", "abcd"]
    expected = ["ab", "abd"]
    result = solution.findWords(board, words)
    assert sorted(result) == sorted(expected), "Test case 3 failed"
    print("Passed")

    # Test case 4: Empty board
    print("Test case 4: Empty board")
    board = []
    words = ["word"]
    expected = []
    result = solution.findWords(board, words)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Empty words list
    print("Test case 5: Empty words list")
    board = [["a", "b"], ["c", "d"]]
    words = []
    expected = []
    result = solution.findWords(board, words)
    assert result == expected, "Test case 5 failed"
    print("Passed")

    # Test case 6: Word not in board
    print("Test case 6: Word not in board")
    board = [["a", "b"], ["c", "d"]]
    words = ["ef"]
    expected = []
    result = solution.findWords(board, words)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_findWords()
