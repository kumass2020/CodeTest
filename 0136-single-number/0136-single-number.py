class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = set()

        for num in nums:
            if num in numbers:
                numbers.remove(num)
            else:
                numbers.add(num)
            
        return next(iter(numbers))