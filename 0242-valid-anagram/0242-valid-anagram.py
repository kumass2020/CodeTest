from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_counts = Counter(s)
        # t_counts = Counter(t)

        # return s_counts == t_counts

        s_dict = {}
        t_dict = {}

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        return s_dict == t_dict