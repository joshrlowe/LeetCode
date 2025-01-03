def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [1, 2]
    i = 3
    while i <= n:
        dp[0], dp[1] = dp[1], dp[0] + dp[1]
        i += 1
    return dp[1]
