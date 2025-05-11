class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        if N <= 1:
            return s

        longest_len = 1
        longest_str = s[0]
        dp = [[False] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = True

            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i]=True
                    if i-j+1 > longest_len:
                        longest_len = i-j+1
                        longest_str = s[j:i+1]


            # for j in range(N+1, i, -1):
            #     new_s = s[i:j]
            #     new_s_rev = new_s[::-1]
            #     # print(new_s, new_s_rev)
            #     if new_s == new_s_rev and len(new_s) > longest_len:
            #         longest_len = len(s[i:j])
            #         longest_str = s[i:j]
            #         break

        return longest_str