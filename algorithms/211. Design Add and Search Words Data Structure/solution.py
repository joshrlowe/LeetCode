class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            cur = node
            for i in range(j, len(word)):
                if word[i] == ".":
                    for c in cur.children:
                        if dfs(cur.children[c], i + 1):
                            return True
                    return False
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            return cur.word

        return dfs(self.root, 0)


def test_WordDictionary():
    # Test case 1: Basic add and search
    print("Test case 1: Basic add and search")
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") == False, "Test case 1 failed: search('pad')"
    assert wd.search("bad") == True, "Test case 1 failed: search('bad')"
    assert wd.search(".ad") == True, "Test case 1 failed: search('.ad')"
    assert wd.search("b..") == True, "Test case 1 failed: search('b..')"
    print("Passed")

    # Test case 2: Search for word not added
    print("Test case 2: Search for word not added")
    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("a")
    assert wd.search("a") == True, "Test case 2 failed: search('a')"
    assert wd.search(".") == True, "Test case 2 failed: search('.')"
    assert wd.search("aa") == False, "Test case 2 failed: search('aa')"
    assert wd.search("a.") == False, "Test case 2 failed: search('a.')"
    assert wd.search(".a") == False, "Test case 2 failed: search('.a')"
    assert wd.search("..") == False, "Test case 2 failed: search('..')"
    print("Passed")

    # Test case 3: Empty WordDictionary
    print("Test case 3: Empty WordDictionary")
    wd = WordDictionary()
    assert wd.search("") == False, "Test case 3 failed: search('')"
    print("Passed")

    # Test case 4: Words with multiple characters and dots
    print("Test case 4: Words with multiple characters and dots")
    wd = WordDictionary()
    wd.addWord("abcd")
    wd.addWord("abce")
    wd.addWord("abcf")
    assert wd.search("abc.") == True, "Test case 4 failed: search('abc.')"
    assert wd.search("ab..") == True, "Test case 4 failed: search('ab..')"
    assert wd.search("a.c.") == True, "Test case 4 failed: search('a.c.')"
    assert wd.search("abcd") == True, "Test case 4 failed: search('abcd')"
    assert wd.search("ab.") == False, "Test case 4 failed: search('ab.')"
    print("Passed")

    # Test case 5: Words with repeated characters
    print("Test case 5: Words with repeated characters")
    wd = WordDictionary()
    wd.addWord("aaa")
    wd.addWord("aab")
    wd.addWord("abb")
    assert wd.search("aaa") == True, "Test case 5 failed: search('aaa')"
    assert wd.search("aab") == True, "Test case 5 failed: search('aab')"
    assert wd.search("abb") == True, "Test case 5 failed: search('abb')"
    assert wd.search("a..") == True, "Test case 5 failed: search('a..')"
    assert wd.search(".a.") == True, "Test case 5 failed: search('.a.')"
    assert wd.search(".b.") == True, "Test case 5 failed: search('.b.')"
    print("Passed")


if __name__ == "__main__":
    test_WordDictionary()
