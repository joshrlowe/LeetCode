from collections import deque


def reverseBits(n: int) -> int:
    binary = deque(bin(n)[2:])
    while len(binary) < 32:
        binary.appendleft("0")
    i, j = 0, len(binary) - 1
    while i <= j:
        binary[i], binary[j] = binary[j], binary[i]
        i += 1
        j -= 1
    return int("".join(binary), 2)
