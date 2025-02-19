# from collections import deque

# def solution(r1, r2):
#     answer = 0
    
#     start = (r2, 0)
#     queue = deque([(r2, 0)])
#     # answer += 1
    
#     moves = [(-1, 0), (0, 1)]
    
#     while queue:
#         answer += 1
#         cx, cy = queue.popleft()
        
#         for move in moves:
#             x = cx + move[0]
#             y = cy + move[1]
            
#             if x > 0 and y < r2:
#                 if r1**2 <= x**2 + y**2 <= r2**2:
#                     # answer += 1
#                     queue.append((x, y))
    
#     answer *= 4
#     return answer
import math

def solution(r1, r2):
    total = 0
    for x in range(0, r2+1):
        lower_sq = r1*r1 - x*x
        
        if lower_sq > 0:
            y_min = math.ceil(math.sqrt(lower_sq))
        else:
            y_min = 0
            
        y_max = math.floor(math.sqrt(r2*r2 - x*x))
        
        if y_max < y_min:
            continue
        
        count_y = y_max - y_min + 1
        
        if x == 0:
            total += count_y * 2
        else:
            if y_min == 0:
                total += 2 + (count_y - 1) * 4
            else:
                total += count_y * 4
    return total