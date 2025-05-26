# from itertools import combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # combs = combinations(candidates)
        # answer = []
        # for comb in combs:
        #     if sum(comb) == Target:
        #         answer.append(comb)
        
        # return answer

        answer = []
        answer_set = set()
        # candidates.sort()

        def dfs(comb, total):
            nonlocal answer
            # print(comb)
            if total == target:
                comb_key = tuple(sorted(comb))
                if comb_key not in answer_set:
                    answer.append(comb[:])
                    answer_set.add(comb_key)
                return
            elif total > target:
                return
            
            new_comb = comb[:]
            for i in range(len(candidates)):
                new_comb.append(candidates[i])
                dfs(new_comb, total+candidates[i])
                new_comb.pop()
    
        dfs([], 0)
        return answer


