def climbStairs(n: int) -> int:
    cache = {}

    def memoization(i):
        if i <= 2:
            return i
        if i in cache:
            return cache[i]
        cache[i] = memoization(i - 1) + memoization(i - 2)
        return cache[i]

    return memoization(n)
