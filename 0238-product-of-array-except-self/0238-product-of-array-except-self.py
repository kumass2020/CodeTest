class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # a = [1 for _ in range(N)]
        # b = [1 for _ in range(N)]
        # # answer = [1 for _ in range(N)]
        # answer = []
        # for i in range(N):
        #     # if i == N-i-1:
        #     #     a = answer[i-1] * nums[i-1] 
        #     #     b = answer[N-i] * nums[N-i] 
        #     #     answer[i] = a * b
        #     # else:
        #     a[i] = a[i-1] * nums[i-1] if i >= 1 else 1
        #     b[N-i-1] = b[N-i] * nums[N-i] if i >= 1 else 1
        
        # # print(a, b)
        # for i in range(N):
        #     answer.append(a[i] * b[i])

        answer = [1] * N
        left = right = 1
        for i in range(1, N):
            left *= nums[i-1]
            answer[i] *= left
        
        for i in range(N-2, -1, -1):
            right *= nums[i+1]
            answer[i] *= right
        
        return answer
