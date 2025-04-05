from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## Using itertools.permutations
        # perms = permutations(nums)
        # return list(perms)

        # DFS
        answer = []

        def dfs(idx, perm):
            if len(perm) == len(nums):
                answer.append(perm[:])

            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    dfs(i+1, perm)
                    perm.pop()

        dfs(0, [])
        return answer
