class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums2 = []
        # for i in range(len(nums)):
        #     if nums2 and nums2[-1] != nums[i]:
        #         nums2.pop()
        #     else:
        #         nums2.append(nums[i])
        
        # return nums2[-1]

        # # Sorting
        # nums.sort()
        # return nums[len(nums)//2]

        # Boyer-Moore
        count = 0
        candidate = None

        for num in nums:
            if not count:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
            