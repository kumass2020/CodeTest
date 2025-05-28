class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # # print(s1,s2,s3)
        # if len(s1)+len(s2) != len(s3):
        #     return False
        
        # if (s1 or s2) and not s3:
        #     return False
        # elif (not s1 and not s2) and s3:
        #     return False
        # elif not s1 and not s2 and not s3:
        #     return True
        

        # result1 = result2 = None
        # # if s1[0] != s3[0] and s2[0] != s3[0]:
        # #     return False
        # if s1 and s1[0] == s3[0]:
        #     result1 = self.isInterleave(s1[1:], s2[:], s3[1:])
        # if s2 and s2[0] == s3[0]:
        #     result2 = self.isInterleave(s1[:], s2[1:], s3[1:])

        # return result1 or result2

        N = len(s1)
        M = len(s2)

        if N == M == len(s3):
            return True
        if N+M != len(s3):
            return False

        dp = [[False] * (M+1) for _ in range(N+1)]
        dp[0][0] = True

        for i in range(1, M+1): # first row, use only s2
            dp[0][i] = dp[0][i-1] and (s2[i-1] == s3[i-1])
        
        for i in range(1, N+1): # first col, use only s1
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])

        for i in range(1, N+1):
            for j in range(1, M+1):
                use_s1 = dp[i-1][j] and (s1[i-1] == s3[i+j-1])
                use_s2 = dp[i][j-1] and (s2[j-1] == s3[i+j-1])

                dp[i][j] = use_s1 or use_s2

        return dp[-1][-1]


        

        

        
