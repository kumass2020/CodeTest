class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')

        if len(pattern) != len(s_list):
            return False
        
        mapping = {}
        for c, s in zip(pattern, s_list):
            # print(c, s)
            if not mapping.get(c):
                if s in mapping.values():
                    return False
                mapping[c] = s
            else:
                if mapping[c] != s:
                     return False

        return True
