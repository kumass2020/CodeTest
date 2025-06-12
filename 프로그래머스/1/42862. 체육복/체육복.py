def solution(n, lost, reserve):
#     answer = 0
#     lost = set(lost)
#     reserve = set(reserve)
    
#     for i in range(1, n+1):
#         if i in lost and i in reserve:
#             lost.remove(i)
#             reserve.remove(i)
#             answer += 1
    
#     for i in range(1, n+1):
#         if i in lost:
#             if i-1 in reserve:
#                 reserve.remove(i-1)
#                 answer += 1
#                 continue
#             elif i+1 in reserve:
#                 reserve.remove(i+1)
#                 answer += 1
#                 continue
#         else:
#             answer += 1
    
#     return answer
                
        
    answer = n-len(lost)
    reserve = set(reserve)
    
    lost2 = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            answer += 1
            continue
        else:
            lost2.append(l)
            
    lost2.sort()
    for l in lost2:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
            continue
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
            continue
        
    return answer