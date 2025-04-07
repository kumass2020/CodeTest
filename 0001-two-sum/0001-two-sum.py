# from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # counts = Counter(nums)
        # for num in nums:
        #     num2 = target - num
        #     if counts.get(num2):

        d = {}
        for i in range(len(nums)):
            num = nums[i]
            lst = d.get(num, [])
            lst.append(i)
            d[num] = lst
        
        print(d)
        for i in range(len(nums)):
            num = nums[i]
            num2 = target - num
        
            if d.get(num2) and d.get(num2)[-1] != i:
                return [i, d.get(num2)[-1]]

