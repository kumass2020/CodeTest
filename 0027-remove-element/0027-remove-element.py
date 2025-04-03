class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        k = 0
        for i in range(N):
            if nums[i] == val:
                nums[i] = -1
                k += 1
        
        nums.sort(reverse=True)
        print(nums)
        return N-k

        # i = 0
        # j = N-1
        
        # while i < N and j >= 0:
        #     while nums[j] != '_':
        #         j -= 1

        #     if nums[i] == '_':
        #         nums[i] = nums[j]
        #         nums[j] = '_'
            
        #     i += 1

        #     if i == j:
        #         return k

        # return k