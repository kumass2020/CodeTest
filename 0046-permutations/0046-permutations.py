from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## Using itertools.permutations
        # perms = permutations(nums)
        # return list(perms)

        # DFS
        answer = []
        used = [False] * len(nums)

        def dfs(idx, perm):
            if len(perm) == len(nums):
                answer.append(perm[:])

            for i in range(len(nums)):
                # if nums[i] not in perm:
                if not used[i]:     # Use boolean array for checking
                    used[i] = True
                    perm.append(nums[i])
                    dfs(i+1, perm)
                    perm.pop()
                    used[i] = False

        dfs(0, [])
        return answer
