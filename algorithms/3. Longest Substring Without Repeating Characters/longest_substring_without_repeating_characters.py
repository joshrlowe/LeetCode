def lengthOfLongestSubstring(s: str) -> int:
    characters = set()
    maxLength, l = 0, 0
    for r in range(len(s)):
        while s[r] in characters:
            characters.remove(s[l])
            l += 1
        characters.add(s[r])
        maxLength = max(maxLength, r - l + 1)

    return maxLength
