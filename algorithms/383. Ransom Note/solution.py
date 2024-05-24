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


def test_can_construct():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    ransomNote1 = "a"
    magazine1 = "b"
    assert solution.canConstruct(ransomNote1, magazine1) == False, "Test Case 1 - Basic functionality test Failed"
    print("Passed")

    # Test Case 2: Exact match
    print("Test Case 2: Exact match")
    ransomNote2 = "aa"
    magazine2 = "aab"
    assert solution.canConstruct(ransomNote2, magazine2) == True, "Test Case 2 - Exact match Failed"
    print("Passed")

    # Test Case 3: More letters in magazine than needed
    print("Test Case 3: More letters in magazine than needed")
    ransomNote3 = "aa"
    magazine3 = "aabb"
    assert solution.canConstruct(ransomNote3, magazine3) == True, "Test Case 3 - More letters in magazine than needed Failed"
    print("Passed")

    # Test Case 4: Not enough letters in magazine
    print("Test Case 4: Not enough letters in magazine")
    ransomNote4 = "aaa"
    magazine4 = "aab"
    assert solution.canConstruct(ransomNote4, magazine4) == False, "Test Case 4 - Not enough letters in magazine Failed"
    print("Passed")

    # Test Case 5: Magazine contains all letters of ransom note
    print("Test Case 5: Magazine contains all letters of ransom note")
    ransomNote5 = "abc"
    magazine5 = "aabbcc"
    assert solution.canConstruct(ransomNote5, magazine5) == True, "Test Case 5 - Magazine contains all letters of ransom note Failed"
    print("Passed")

    # Test Case 6: Empty ransom note
    print("Test Case 6: Empty ransom note")
    ransomNote6 = ""
    magazine6 = "abc"
    assert solution.canConstruct(ransomNote6, magazine6) == True, "Test Case 6 - Empty ransom note Failed"
    print("Passed")

    # Test Case 7: Empty magazine
    print("Test Case 7: Empty magazine")
    ransomNote7 = "a"
    magazine7 = ""
    assert solution.canConstruct(ransomNote7, magazine7) == False, "Test Case 7 - Empty magazine Failed"
    print("Passed")

    # Test Case 8: Ransom note contains repeating letters
    print("Test Case 8: Ransom note contains repeating letters")
    ransomNote8 = "aaabb"
    magazine8 = "aabbaa"
    assert solution.canConstruct(ransomNote8, magazine8) == True, "Test Case 8 - Ransom note contains repeating letters Failed"
    print("Passed")

    # Test Case 9: Magazine and ransom note are the same
    print("Test Case 9: Magazine and ransom note are the same")
    ransomNote9 = "abc"
    magazine9 = "abc"
    assert solution.canConstruct(ransomNote9, magazine9) == True, "Test Case 9 - Magazine and ransom note are the same Failed"
    print("Passed")

    # Test Case 10: Magazine has multiple of the same letter, but ransom note has more
    print("Test Case 10: Magazine has multiple of the same letter, but ransom note has more")
    ransomNote10 = "aaaa"
    magazine10 = "aaab"
    assert solution.canConstruct(ransomNote10, magazine10) == False, "Test Case 10 - Magazine has multiple of the same letter, but ransom note has more Failed"
    print("Passed")

if __name__ == "__main__":
    test_can_construct()
