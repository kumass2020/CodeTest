class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.replace("  ", " ").split(" ")
        # print(s_list)

        i = len(s_list)-1
        while i >= 0:
            if s_list[i] != '':
                return len(s_list[i])
            i -= 1