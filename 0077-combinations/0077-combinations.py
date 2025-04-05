from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ## using itertools.combniations
        # if n == 1:
        #     return [[n]]
        # lst = [i for i in range(1, n+1)]
        # combs = list(combinations(lst, k))
        # return combs


        # using DFS
        answer = []
        def dfs(idx, comb):
            # print(comb)
            nonlocal answer
            
            if len(comb) == k:
                print(comb)
                answer.append(comb[:])
                return

            for i in range(idx, n+1):
                comb.append(i)
                dfs(i+1, comb)
                comb.pop()

        dfs(1, [])
        return answer
        