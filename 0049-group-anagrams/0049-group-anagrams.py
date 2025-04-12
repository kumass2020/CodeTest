from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # N = len(strs)

        # if N == 0:
        #     return [['']]
        # elif N == 1:
        #     return [strs]
        

        # # print(Counter(strs[0]) == Counter(strs[1]))
        # answer = []
        # counters = []
        # for s in strs:
        #     s_counter = Counter(s)
        #     if not answer:
        #         answer.append([s])
        #         counters.append(s_counter)
        #     else:
        #         flag = 0
        #         # for i, a in enumerate(answer):
        #         #     if Counter(a[0]) == Counter(s):
        #         #         answer[i].append(s)
        #         #         flag = 1
        #         #         break
        #         for i, c in enumerate(counters):
        #             if c == s_counter:
        #                 answer[i].append(s)
        #                 flag = 1
        #                 break
        #             # if i-1 == len(answer):
        #         if not flag:
        #             answer.append([s])
        #             counters.append(s_counter)
            
        # return answer


        answer = []
        sorts = []
        for s in strs:
            sorted_s = sorted(s)
            if not answer:
                answer.append([s])
                sorts.append(sorted_s)
            else:
                flag = 0
                # for i, a in enumerate(answer):
                #     if sorted_s == sorted(a[0]):
                #         answer[i].append(s)
                #         flag = 1
                #         break
                for i, a in enumerate(sorts):
                    if sorted_s == a:
                        answer[i].append(s)
                        flag = 1
                        break
                
                if not flag:
                    answer.append([s])
                    sorts.append(sorted_s)
        
        return answer

