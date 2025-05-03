class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            i = 0
            while i < len(prefix) and i < len(s):
                if prefix[i] != s[i]:
                    if i >= 1:
                        prefix = prefix[:i]
                        break
                    else:
                        return ""
                i += 1
            prefix = prefix[:i]
        
        return prefix
                