class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(haystack)
        M = len(needle)
        for i in range(N-M+1):
            if haystack[i:i+M] == needle:
                return i
        return -1