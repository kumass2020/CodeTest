class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # dp = [float('inf') for _ in range(len(triangle))]
        # dp[0] = triangle[0][0]
        # prev_idx = 0
        # for i in range(1, len(triangle)):
        #     row = triangle[i]
        #     for prev_idx in [i, i+1]:
        #         dp[i] = dp[i-1] + row[prev_idx]
        #     prev_idx += 1
        #     # if row[prev_idx] < row[prev_idx+1]:
        #     #     dp[i] = dp[i-1] + row[prev_idx]
        #     # else:
        #     #     dp[i] = dp[i-1] + row[prev_idx+1]
        #     #     prev_idx += 1

        # def dfs():
        #     if idx == len(triangle)-1:
        #         dp[-1] = min(dp[-1], summ)

        #     for i in [prev_idx, prev_idx+1]:
        #         summ += triangle[]
        #         dfs(i)

        # return dp[-1]
            
        triangle_sum = [[0] * i for i in range(1, len(triangle)+1)]
        triangle_sum[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # print(i, j)
                if j == 0:
                    triangle_sum[i][j] = triangle_sum[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle_sum[i][j] = triangle_sum[i-1][j-1]
                else:
                    triangle_sum[i][j] = min(triangle_sum[i-1][j-1], triangle_sum[i-1][j])
                triangle_sum[i][j] += triangle[i][j]
                
        return min(triangle_sum[-1])

            