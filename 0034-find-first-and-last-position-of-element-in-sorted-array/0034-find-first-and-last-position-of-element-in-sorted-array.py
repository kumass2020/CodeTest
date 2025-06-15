class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        start = end = None

        if right == -1:
            return [-1, -1]
        elif right == 0:
            return [0, 0] if target == nums[0] else [-1, -1]

        def bin_search(left, right, nums):
            nonlocal start, end, target

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid+1
                
                elif nums[mid] > target:
                    right = mid-1

                elif nums[mid] == target:
                    prev_left = left
                    prev_mid = mid
                    left_nums = nums[left:mid+1]
                    right_nums = nums[mid:right+1]

                    # print(mid, left, right)
                    # print(left_nums, right_nums)

                    left = 0
                    right = len(left_nums)-1
                    # start = bin_search(left, right, left_nums)
                    while left <= right:
                        mid = (left + right) // 2
                        
                        if left_nums[mid] == target:
                            if mid >= 1 and left_nums[mid] != left_nums[mid-1]:
                                start = prev_left + mid 
                                break
                            elif mid == 0:
                                start = prev_left + mid 
                                break
                            else:
                                right = mid-1
                        elif left_nums[mid] < target:
                            left = mid+1


                    left = 0
                    right = len(right_nums)-1
                    while left <= right:
                        mid = (left + right) // 2

                        if right_nums[mid] == target:
                            if mid < len(right_nums)-1 and right_nums[mid] != right_nums[mid+1]:
                                end = prev_mid + mid
                                break
                            elif mid == len(right_nums)-1:
                                end = prev_mid + mid
                                break
                            else:
                                left = mid+1
                        elif right_nums[mid] > right:
                            right = mid-1
                    
                    break    


                    # end = bin_search(left, right, right_nums)

                    # while left < right:
                        # mid = (left + right) // 2
                    

        bin_search(left, right, nums)
        # print(start, end)

        if start is not None or end is not None:
            return [start, end]
        else:
            return [-1, -1]
        


        

                    
            

