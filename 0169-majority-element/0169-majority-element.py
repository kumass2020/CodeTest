class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums2 = []
        for i in range(len(nums)):
            if nums2 and nums2[-1] != nums[i]:
                nums2.pop()
            else:
                nums2.append(nums[i])
        
        return nums2[-1]
            