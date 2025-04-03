class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # i = 0
        # j = 0

        # mapping = {}
        # while i < len(s) and j < len(t):

        mapping = {}
        new_s = ''
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if not mapping.get(char_s):
                if char_t in mapping.values():
                    return False
                mapping[char_s] = char_t
            else:
                if mapping[char_s] != char_t:
                    return False
            # print(mapping)

            new_s += mapping[char_s]
            # print(new_s)
            # t.replace(char_t, char_s)

        # for key, value in mapping.items():
        #     t = t.replace(value, key)
        #     print(value, key, t)


        if new_s == t:
            return True
        else:
            return False

            