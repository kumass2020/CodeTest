class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        k = 0
        for i in range(N):
            if nums[i] == val:
                # nums[i] = -1
                nums[i] = '_'
                k += 1
        
        # nums.sort(reverse=True)
        # print(nums)
        # return N-k

        i = 0
        j = N-1
        
        while i < j:
            while j >= 0 and nums[j] == '_':
                j -= 1

            # print(nums, i, j)
            
            if nums[i] == '_':
                nums[i] = nums[j]
                nums[j] = '_'
            
            # if i == j:
            #     return N-k

            i += 1



        return N-k