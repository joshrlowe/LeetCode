class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


def test_trie():
    # Test case 1: Basic insert and search
    print("Test case 1: Basic insert and search")
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True, "Test case 1 failed: search('apple')"
    assert trie.search("app") == False, "Test case 1 failed: search('app')"
    assert trie.startsWith("app") == True, "Test case 1 failed: startsWith('app')"
    trie.insert("app")
    assert (
        trie.search("app") == True
    ), "Test case 1 failed: search('app') after insert('app')"
    print("Passed")

    # Test case 2: Insert multiple words and search
    print("Test case 2: Insert multiple words and search")
    trie = Trie()
    words = ["hello", "hell", "heaven", "heavy"]
    for word in words:
        trie.insert(word)
    assert trie.search("hello") == True, "Test case 2 failed: search('hello')"
    assert trie.search("hell") == True, "Test case 2 failed: search('hell')"
    assert trie.search("heaven") == True, "Test case 2 failed: search('heaven')"
    assert trie.search("heavy") == True, "Test case 2 failed: search('heavy')"
    assert trie.search("he") == False, "Test case 2 failed: search('he')"
    assert trie.startsWith("he") == True, "Test case 2 failed: startsWith('he')"
    print("Passed")

    # Test case 3: Search for non-existent word
    print("Test case 3: Search for non-existent word")
    trie = Trie()
    trie.insert("word")
    assert trie.search("words") == False, "Test case 3 failed: search('words')"
    assert trie.startsWith("wor") == True, "Test case 3 failed: startsWith('wor')"
    assert trie.startsWith("wordy") == False, "Test case 3 failed: startsWith('wordy')"
    print("Passed")

    # Test case 4: Empty Trie
    print("Test case 4: Empty Trie")
    trie = Trie()
    assert trie.search("") == False, "Test case 4 failed: search('')"
    assert trie.startsWith("") == True, "Test case 4 failed: startsWith('')"
    print("Passed")

    # Test case 5: Insert and search single character words
    print("Test case 5: Insert and search single character words")
    trie = Trie()
    trie.insert("a")
    trie.insert("b")
    assert trie.search("a") == True, "Test case 5 failed: search('a')"
    assert trie.search("b") == True, "Test case 5 failed: search('b')"
    assert trie.search("c") == False, "Test case 5 failed: search('c')"
    assert trie.startsWith("a") == True, "Test case 5 failed: startsWith('a')"
    assert trie.startsWith("b") == True, "Test case 5 failed: startsWith('b')"
    assert trie.startsWith("c") == False, "Test case 5 failed: startsWith('c')"
    print("Passed")


if __name__ == "__main__":
    test_trie()
