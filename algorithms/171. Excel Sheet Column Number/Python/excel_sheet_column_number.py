def titleToNumber(columnTitle: str) -> int:
    numLetter = {chr(i): i - 64 for i in range(65, 91)}

    i = len(columnTitle) - 1
    j = 1
    res = 0
    while i >= 0:
        res += numLetter[columnTitle[i]] * j
        i -= 1
        j *= 26
    return res
