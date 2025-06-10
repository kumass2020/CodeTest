class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        
        N, M = len(nums1), len(nums2)
        heap = []

        for i in range(min(N, k)):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        
        answer = []
        while heap and len(answer) != k:
            summ, i, j = heapq.heappop(heap)
            answer.append((nums1[i], nums2[j]))

            print(summ, i, j)

            if j < M-1:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))

        return answer

        # from collections import defaultdict
        # dt = defaultdict(list)
        # for num1 in nums1:
        #     for num2 in nums2:
        #         dt[num1+num2].append((num1, num2))
        
        # # print(dt, list(dt.keys()))
        
        # lst = list(dt.keys())
        # lst.sort()
        # answer = []
        # for i, key in enumerate(lst):
            
        #     for pair in dt[key]:
        #         answer.append(pair)

        #         if len(answer) == k:
        #             return answer

        # # return answer