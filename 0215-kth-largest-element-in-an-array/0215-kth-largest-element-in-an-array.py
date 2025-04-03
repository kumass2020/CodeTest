import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq, -num)

        print(hq)

        for i in range(k):
            last_val = -heapq.heappop(hq)
        return last_val