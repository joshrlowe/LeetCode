class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magLetters = {}
        for letter in magazine:
            magLetters[letter] = magLetters.get(letter, 0) + 1
        for letter in ransomNote:
            if letter not in magLetters or magLetters[letter] == 0:
                return False
            magLetters[letter] -= 1
        return True
