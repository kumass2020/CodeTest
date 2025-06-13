class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif not s or not t:
            return False

        i = j = 0

        while i <= len(s)-1 and j <= len(t)-1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        # print(i, j)

        if i != len(s):
            return False
        elif i >= len(s):
            return True

        # idx = -1
        # # for c in s:
        # #     print(idx, t)
        # #     c_idx = t.index(c)
        # #     if idx >= c_idx:
        # #         return False
        # #     idx = c_idx
        # # return True

        # if len(s) == 0:
        #     return True
        # if len(t) == 0 and len(s) > 0:
        #     return False

        # i = 0
        # for c in t:
        #     # print(c)
        #     if c == s[i]:
        #         # print(s[i], i)
        #         i += 1
        #         if i == len(s):
        #             return True
        # return False
            
        