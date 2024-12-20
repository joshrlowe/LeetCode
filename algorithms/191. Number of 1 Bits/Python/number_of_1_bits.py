def hammingWeight(n: int) -> int:
    binary = bin(n)[2:]
    result = 0
    for digit in binary:
        if digit == "1":
            result += 1
    return result
