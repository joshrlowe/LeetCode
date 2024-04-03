class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-0.5 + (0.25 + 2 * n) ** 0.5)
