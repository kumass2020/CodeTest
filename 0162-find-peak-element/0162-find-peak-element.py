class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return 0

        left = 0
        right = N-1
        
        while left <= right:
            mid = (left+right) // 2
            # print(mid)

            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
            elif mid == N-1:
                if nums[mid] > nums[mid-1]:
                    return mid

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
            

        # return False