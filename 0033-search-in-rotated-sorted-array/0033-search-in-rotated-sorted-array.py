class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        low, high = 0, N-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:   # left sorted
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:   # right sorted
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
                
            



        # # find starting point by binary search
        # mid = nums[N//2]
        # while True:
        #     left = nums[:N//2]

        # # recover sorted array

        # # find target by binary search
