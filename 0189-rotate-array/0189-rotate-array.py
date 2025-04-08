from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        q = deque(nums)
        for i in range(k):
            q.appendleft(q[-1])
            q.pop()
            # print(q)
        nums[:] = list(q)