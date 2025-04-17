from collections import deque
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        dp = [[0] * N for _ in range(M)]
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0

        for i in range(M):
            for j in range(N):
                if not (i == 0 and j == 0) and not obstacleGrid[i][j]:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left
                # dp[i][j] = dp[i-1][j] + dp[i][j-1]


        # # dp[0][0] = 1
        # moves = [(1, 0), (0, 1)]

        # q = deque()
        # q.append((0, 0))
        # while q:
        #     i, j = q.popleft()
        #     # print(i, j)

        #     if i == 0 and j == 0:
        #         dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        #     else:
        #         up = dp[i-1][j] if i > 0 else 0
        #         left = dp[i][j-1] if j > 0 else 0
        #         dp[i][j] = up + left

        #     for move in moves:
        #         ni = i + move[0]
        #         nj = j + move[1]

        #         if 0 <= ni <= M-1 and 0 <= nj <= N-1 and not dp[ni][nj] and not obstacleGrid[ni][nj]:
        #             q.append((ni, nj))

        return dp[-1][-1]
