from itertools import combinations, product
import bisect 

def solution(dice):
    answer = []
    N = len(dice)
    
    # 각 주사위의 모든 경우의 수 계산 -> 다른 주사위의 경우의 수와 비교, 승리 count
    count = 0
    
    win_case = []
    dice_idx = [i for i in range(N)]
    dvx = [0, 1, 2, 3, 4, 5]
    
    comb = list(combinations(dice_idx, N // 2))
    perm = list(product(range(6), repeat=N//2))
    # print(list(comb))
    
    # 내가 뽑은 주사위와 아닌 주사위를 나누고
    for c in comb:
        a = c
        b = dice_idx[:]
        for elem in c:
            b.remove(elem)
        
        result_a = []
        result_b = []
        dice_a = []
        dice_b = []
        
        for i in range(N // 2):
            dice_a.append(dice[a[i]])
            dice_b.append(dice[b[i]])
        
        for p in perm:
            result = 0
            for i in range(N // 2):
                result += dice_a[i][p[i]]
            result_a.append(result)
            
            result = 0
            for i in range(N // 2):
                result += dice_b[i][p[i]]
            result_b.append(result)
                

        result_a = sorted(result_a)
        result_b = sorted(result_b)

        win_count = 0
        for val_a in result_a:
            idx = bisect.bisect_left(result_b, val_a)
            win_count += idx

        
        # win_count = 0
        # for val_a in result_a:
        #     for i, val_b in enumerate(result_b):
        #         if val_a > val_b:
        #             win_count += len(result_b)-i
        #             break
                # else:
                    # val_a > all val_b
                    # win_count += len(result_b)
                    
        win_case.append(win_count)
    
    max_val = max(win_case)
    idx = win_case.index(max_val)
    answer = list(comb[idx])
    for i in range(len(answer)):
        answer[i] += 1
    return answer
                
            # for j in range(len(result_a)):
                
            
    
    
#     def dfs(idx, lst):
#         if len(lst) == N // 2:
            
        
#         for i in range(N):
#             lst.append(dice[i])
#             dfs(idx+1, lst)
#             lst.pop()
            
                    
                    
    
    
    
    # return answer