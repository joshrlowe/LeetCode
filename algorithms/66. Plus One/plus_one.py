from typing import List


def plusOne(digits: List[int]) -> List[int]:
    i = len(digits) - 1
    while i > -1:
        digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            i -= 1
        else:
            break
    if i == -1:
        digits[0] = 1
        digits.append(0)
    return digits
