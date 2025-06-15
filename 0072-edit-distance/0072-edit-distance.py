class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # dp[i][j] -> word1의 처음 i글자(word1[0..i-1])를 word2의 처음 j글자(word2[0..j-1])로 바꾸는 최소 편집 횟수
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )
                    
        return dp[n][m]
        
