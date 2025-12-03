class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = len(nums)-1
        # mid = (left + right) // 2

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid
            elif num < target:
                left = mid+1
            else:
                right = mid-1
            
        return -1