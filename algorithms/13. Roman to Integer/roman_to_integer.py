def romanToInt(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_sum = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
            roman_sum += values[s[i + 1]] - values[s[i]]
            i += 2
        else:
            roman_sum += values[s[i]]
            i += 1
    return roman_sum
