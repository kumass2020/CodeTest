class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dist = -1
        for i, num in enumerate(nums):
            max_dist = max(max_dist, num + i)
            if i != len(nums)-1 and max_dist <= i:
                return False
        
        return True