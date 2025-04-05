class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        j = 1
        # while i < len(nums):
        counter = 0
        while j < len(nums):
            if nums[j-1] == nums[j]:
                counter += 1
                if counter >= 2:
                    j += 1
                    continue
            else:
                counter = 0
                
            nums[i] = nums[j]
            i += 1
            j += 1
        
        return i



            
