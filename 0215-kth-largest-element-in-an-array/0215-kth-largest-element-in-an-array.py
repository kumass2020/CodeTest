import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # hq = []
        # heapq.heapify(nums)
        # print(nums)
        # for num in nums:
        #     heapq.heappush(hq, -num)

        # # print(hq)

        # for i in range(k):
        #     last_val = -heapq.heappop(hq)
        # return last_val

        hq = nums[:k]
        heapq.heapify(hq)

        for num in nums[k:]:
            if num > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, num)
            
        return hq[0]