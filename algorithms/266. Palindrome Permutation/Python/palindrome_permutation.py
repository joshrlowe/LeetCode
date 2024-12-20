from collections import Counter


def canPermutePalindrome(s: str) -> bool:
    freq = Counter(s)
    odd = 0
    for _, f in freq.items():
        if f % 2 == 1:
            odd += 1
    return odd <= 1
