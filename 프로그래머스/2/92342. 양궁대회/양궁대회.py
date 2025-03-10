# def solution(n, info):
#     answer = []
    
#     scores = [0 for i in range(11)]
#     stack = []
    
#     # 라이언의 모든 점수의 경우 계산
#     def dfs(stack, score):
#         if sum(scores) == n:
#             # 점수 차 계산
            
        
#             # 점수 차가 똑같을 경우 가장 낮은 점수를 많이 맞힌 경우를 선택
            
        
#         for i in range(11):
#             stack.append(i)
#             scores[i] += 1
#             dfs(stack, score)
#             scores[i] -= 1
#             stack.pop()

    
#     return answer

import math

def solution(n, info):
    best_diff = 0
    best_alloc = [-1]
    
    alloc = [0] * 11
    
    def dfs(i, remain):
        nonlocal best_diff, best_alloc, alloc
        if i == 10:
            alloc[i] = remain
            
            ryan_score = 0
            apeach_score = 0
            for j in range(11):
                score = 10 - j
                
                if alloc[j] > info[j]:
                    ryan_score += score
                elif info[j] > 0:
                    apeach_score += score
            diff = ryan_score - apeach_score
        
            if diff > 0:
                if diff > best_diff:
                    best_diff = diff
                    best_alloc = alloc.copy()
                elif diff == best_diff:
                    for j in range(10, -1, -1):
                        if alloc[j] > best_alloc[j]:
                            best_alloc = alloc.copy()
                            break
                        elif alloc[j] < best_alloc[j]:
                            break
            
            return
        
        for arrows in range(remain + 1):
            alloc[i] = arrows
            dfs(i + 1, remain - arrows)
            alloc[i] = 0
    
    dfs(0, n)
    
    return best_alloc if best_alloc[0] != -1 else [-1]