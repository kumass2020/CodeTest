import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        pc = []
        for p, c in zip(profits, capital):
            pc.append((p, c))
        
        pc.sort(key=lambda x: x[1])
        # pc.sort(key=lambda x: (x[1], -x[0]))

        # for i in range(k):
        #     # has minimal capital
        #     for i, (p, c) in enumerate(pc):
        #         if w >= c:
        #             # choose best profit
        #             w += p
        #             pc = pc[i:]
        #             break

        # return w
        print(pc)
            
        heap = []
        i = 0
        while k > 0:
            
            while i < len(pc):
                p, c = pc[i]
                if w < c:
                    break

                heapq.heappush(heap, -p)

                i += 1
            
            if not heap:
                break
            
            w += -heapq.heappop(heap)
            k -= 1
        
        return w
