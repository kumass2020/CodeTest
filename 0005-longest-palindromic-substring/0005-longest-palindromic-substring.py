class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest_len = -1
        longest_str = ''
        for i in range(N):
            for j in range(N+1, i, -1):
                new_s = s[i:j]
                new_s_rev = new_s[::-1]
                # print(new_s, new_s_rev)
                if new_s == new_s_rev and len(new_s) > longest_len:
                    longest_len = len(s[i:j])
                    longest_str = s[i:j]
                    break

        return longest_str