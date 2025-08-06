#Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
#Top down
class Solution:
        def climbStairs(self, n: int) -> int:
            memo = {}
            def dp(i):
                if i > n:
                    return 0
                if i == n:
                    return 1
                if i in memo:
                    return memo[1]
                memo[i] = dp(i + 1) + dp(i + 2)
                return memo[i]
            return dp(0)