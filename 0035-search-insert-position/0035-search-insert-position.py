class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        # if nums[0] >= target:
        #     return 0
        
        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]

            if val == target:
                return mid
            elif val > target:
                right = mid-1
            else:
                left = mid+1

        # if len(nums) == 1:
        #     if nums[0] >= target:
        #         return 0
        #     else:
        #         return 1

        # print(mid, val, left, right)
        return left
            
        

