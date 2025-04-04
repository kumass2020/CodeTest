class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # memory = 101
        # k = len(nums)
        # for i in range(len(nums)):
        #     num = nums[i]
        #     if memory == num:
        #         nums[i] = 101
        #         k -= 1
        #     memory = num

        # nums.sort()

        # return k
        
        # L = len(nums)

        # # i = 0
        # j = 0
        # memory = 101
        # for i in range(len(nums)):
        #     if nums[j] == memory:
        #         nums[j] = '_'

        #     while j < len(nums)-1 and nums[j] != '_':
        #         j += 1

        #     if i+1 < len(nums):
        #         nums[i+1] = nums[j]
        #         nums[j] = '_'

        #     if nums[i] == '_':
        #         return i

        #     memory = nums[j]

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        
        return j
            
