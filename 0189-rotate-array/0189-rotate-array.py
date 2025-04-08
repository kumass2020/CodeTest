from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # q = deque(nums)
        # for i in range(k):
        #     q.appendleft(q[-1])
        #     q.pop()
        #     # print(q)
        # nums[:] = list(q)

        k = k % len(nums)
        # temp = [0 for _ in range(k)]
        
        temp = nums[-k:]
        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        for j in range(k):
            nums[j] = temp[j]

        