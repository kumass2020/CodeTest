import heapq
def solution(scoville, K):
    # answer = 0
    
    heapq.heapify(scoville)
    hq = scoville
    # print(scoville)
    
    N = len(scoville)
    for i in range(N):
        a = heapq.heappop(hq)
        
        if a >= K:
            return i
        if i == N-1:
            return -1 if b < K else N-1
        
        b = heapq.heappop(hq)
        heapq.heappush(hq, a+b*2)
    
    return -1
        
    
    # return answer