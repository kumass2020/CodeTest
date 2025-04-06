class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = -1
        # for c in s:
        #     print(idx, t)
        #     c_idx = t.index(c)
        #     if idx >= c_idx:
        #         return False
        #     idx = c_idx
        # return True

        if len(s) == 0:
            return True
        if len(t) == 0 and len(s) > 0:
            return False

        i = 0
        for c in t:
            # print(c)
            if c == s[i]:
                # print(s[i], i)
                i += 1
                if i == len(s):
                    return True
        return False
            
        