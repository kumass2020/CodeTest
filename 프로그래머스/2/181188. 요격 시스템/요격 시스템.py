# from collections import Count

def solution(targets):
#     misile = 0
#     # x_dict = {x: 0 for x in range(100000000+1)}
#     x_dict = {}
    
#     for target in targets:
#         for x in range(target[0]+1, target[1]):
#             x_dict[x] = x_dict.get(x, 0) + 1
    
#     while True:
#         max_key = max(x_dict, key=x_dict.get)
#         for target in targets:
#             if target[0]+1 <= max_key <= target[1]:
#                 for x in range(target[0]+1, target[1]):
#                     x_dict[x] -= 1
#         misile += 1
            
#         if max(x_dict.values()) == 0:
#             return misile
    targets.sort(key=lambda interval: interval[1])
    
    missiles = 0
    
    last_missile = -float('inf')
    
    for s, e in targets:
        if not (s < last_missile < e):
            last_missile = e - 0.5
            missiles += 1
    
    return missiles