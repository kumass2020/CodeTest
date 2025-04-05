from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[n]]
        lst = [i for i in range(1, n+1)]
        combs = list(combinations(lst, k))
        return combs
        