class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        longest_substring_length = 0
        start, end = 0, 0
        while end < len(s):
            if s[end] in characters:
                if end - start > longest_substring_length:
                    longest_substring_length = end - start
                while s[start] != s[end]:
                    characters.discard(s[start])
                    start += 1
                characters.discard(s[start])
                start += 1
            characters.add(s[end])
            end += 1
        if end - start > longest_substring_length:
            longest_substring_length = end - start
        return longest_substring_length