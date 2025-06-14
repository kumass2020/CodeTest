class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        A = [0] * N
        answer = A[0] = nums[0]

        # i = j = 0
        for i in range(1, N):
            A[i] = max(A[i-1]+nums[i], nums[i])
            answer = max(answer, A[i])
        
        return answer

