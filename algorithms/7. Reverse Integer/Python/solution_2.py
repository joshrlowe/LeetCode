class Solution:
    def reverse(self, x: int) -> int:
        x = -1 * int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        return x if x.bit_length() < 32 else 0