from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = permutations(nums)
        return list(perms)