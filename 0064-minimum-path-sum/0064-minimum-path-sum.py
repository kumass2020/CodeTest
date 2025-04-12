class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])

        dp = [[0] * N] * M
        dp[0][0] = grid[0][0]

        # dp[0] = grid[0]
        # for i in range(M):
        #     dp[i][0] = grid[i][0]

        for i in range(M):
            for j in range(N):
                up = dp[i-1][j] if i >= 1 else 201
                left = dp[i][j-1] if j >= 1 else 201

                # print(i, j, up, left, min(up, left) + grid[i][j])

                if i == 0 and j == 0:
                    pass
                else:
                    dp[i][j] = min(up, left) + grid[i][j]

        return dp[-1][-1]
