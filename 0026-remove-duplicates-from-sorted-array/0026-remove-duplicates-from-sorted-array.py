class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        memory = 101
        k = len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if memory == num:
                nums[i] = 101
                k -= 1
            memory = num

        nums.sort()

        return k