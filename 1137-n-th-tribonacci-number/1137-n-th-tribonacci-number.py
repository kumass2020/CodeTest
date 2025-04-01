class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # print(dp)
        # print(dp[0])
        # print(dp[1])
        # print(dp[2])
        # print(dp[3])
        if n >= 3:
            for i in range(n-2):
                # print(i)
                dp[i+3] = dp[i] + dp[i+1] + dp[i+2]
        
        return dp[n]