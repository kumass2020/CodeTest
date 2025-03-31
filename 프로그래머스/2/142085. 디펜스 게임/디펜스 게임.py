# def solution(n, k, enemy):
#     answer = 0
    
#     my = []
#     sum_my = 0
#     for i, new in enumerate(enemy):
#         # print(sum_my)
#         # print(my)
#         my.append(new)
            
#         if sum_my + new > n:
#             if k >= 1:
#                 my.sort(reverse=True)
        
#                 if i > k:
#                     my = my[:k]
                
#                 k -= 1
#                 max_my = my[0]
#                 my.pop(0)
#                 sum_my = sum_my + new - max_my
#             else:
#                 return i
#         else:
#             sum_my += new
    
#     return i+1


import heapq

def solution(n, k, enemy):
    total = 0
    max_heap = []
    
    for i, count in enumerate(enemy):
        total += count
        
        heapq.heappush(max_heap, -count)
        
        if total > n:
            if k > 0:
                total += heapq.heappop(max_heap)
                k -= 1
            else:
                return i
    
    return len(enemy)