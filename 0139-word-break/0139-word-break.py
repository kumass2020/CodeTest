class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cstr = ''
        # def match(i, cstr):
        #     # for i in range(len(s)):
        #     # print(i, cstr)
        #     cstr += s[i]
        #     for word in wordDict:
        #         if word == cstr:
        #             if i+1 < len(s):
        #                 return match(i+1, '') or match(i+1, cstr)
        #             else:
        #                 return True
                    
        #     if i+1 < len(s):
        #         return match(i+1, cstr)
        #     else:
        #         return True if not cstr else False
        
        # return match(0, '')

        word_set = set(wordDict)
        memo = {}

        def can_break(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for word in word_set:
                if s.startswith(word, start):
                    if can_break(start+len(word)):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False

        return can_break(0)
                    
