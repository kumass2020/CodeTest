class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return 0
        elif N == 2:
            return 1

        steps = 0
        i = 0
        while i < N:
            if i == N-1:
                return steps

            reachable = nums[i] + i

            if reachable >= N-1:
                return steps+1

            max_reachable = -1
            next_i = -1
            for j in range(i+1, min(reachable, N-1)+1):
                # print(i, j, min(reachable, N), reachable, nums[j]+j, max_reachable)
                if nums[j]+j > max_reachable:
                    max_reachable = nums[j]+j
                    next_i = j
                # max_reachable = max(max_reachable, nums[j]+j)
            
            print(max_reachable, steps, next_i)
            # if max_reachable >= N-1:
            #     return steps+1
            # else:
            i = next_i
            steps += 1
            
                
