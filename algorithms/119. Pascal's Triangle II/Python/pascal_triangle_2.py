import math
from typing import List


def nCk(n: int, k: int) -> int:
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def getRow(rowIndex: int) -> List[int]:
    res = []
    for k in range(rowIndex + 1):
        res.append(nCk(rowIndex, k))
    return res
