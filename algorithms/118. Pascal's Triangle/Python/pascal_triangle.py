from typing import List


def generate(numRows: int) -> List[List[int]]:
    def constructLevel(prevRow):
        level = [1]
        for i in range(1, len(prevRow)):
            level.append(prevRow[i] + prevRow[i - 1])
        level.append(1)
        return level

    res = [[1]]
    for i in range(1, numRows):
        res.append(constructLevel(res[-1]))
    return res
