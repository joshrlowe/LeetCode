def lengthOfLastWord(s: str) -> int:
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1

    res = 0
    while i >= 0 and s[i] != " ":
        i -= 1
        res += 1

    return res
