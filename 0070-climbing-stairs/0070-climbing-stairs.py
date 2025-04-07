class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for _ in range(n)]
        
        if n == 1:
            return 1
        elif n == 2:
            return 2

        ways[0] = 1
        ways[1] = 2


        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n-1]