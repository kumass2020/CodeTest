class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s_list = s.split(' ')

        # if len(pattern) != len(s_list):
        #     return False
        
        # mapping = {}
        # for c, s in zip(pattern, s_list):
        #     # print(c, s)
        #     if not mapping.get(c):
        #         if s in mapping.values():
        #             return False
        #         mapping[c] = s
        #     else:
        #         if mapping[c] != s:
        #              return False

        # return True

        s_list = s.split(' ')
        dt = {}

        if len(s_list) != len(pattern):
            return False

        for i, word in enumerate(s_list):
            c = pattern[i]

            if not dt.get(c):
                if word in dt.values():
                    return False
                dt[c] = word
            else:
                if dt[c] != word:
                    return False
        
        return True
