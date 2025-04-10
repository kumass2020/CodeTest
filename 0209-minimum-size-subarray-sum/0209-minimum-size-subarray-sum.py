class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        answer = 100001        
        for i in range(len(nums)):
            j = i
            summ = 0 

            while j < len(nums) and summ < target and j-i < answer:
                summ += nums[j]
                j += 1
            
            if j == len(nums) and summ < target:
                continue
            
            # print(answer, i, j, j-i)
            answer = min(answer, j-i)
        return answer if answer != 100001 else 0
        