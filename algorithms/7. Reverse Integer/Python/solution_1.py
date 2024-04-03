class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        reversed = 0
        while x > 0:
            reversed += x % 10
            x -= x % 10
            x /= 10
            reversed *= 10
        x = -1 * int(reversed // 10) if negative else int(reversed // 10)
        return x if x.bit_length() < 32 else 0
