def solution(info, n, m):
    answer = 0
    
#     # steal = []
#     min_A = 121
#     # visited = [[0, 0] for i in range(len(info))]
#     def dfs(idx, steal, A, B):
#         nonlocal min_A
#         new_steal = steal[:]
        
#         if idx == len(info):
#             if A < min_A:
#                 min_A = A
#         else:
#         # for i in range(idx, len(info)):
#             for stealer in ['B', 'A']:
#                 if stealer == 'A' and A + info[idx][0] < n:
#                     A += info[idx][0]
#                     new_steal.append([stealer, info[idx][0]])
#                 elif stealer == 'B' and B + info[idx][1] < m:
#                     B += info[idx][1]
#                     new_steal.append([stealer, info[idx][1]])
#                 else:
#                     continue

#                 # print(new_steal)
#                 dfs(idx+1, new_steal, A, B)        
#                 new_steal.pop()
#                 if stealer == 'A':
#                     A -= info[idx][0]
#                 else:
#                     B -= info[idx][1]
                
    
#     dfs(0, [], 0, 0)

#     # n_info = info
#     # n_info.sort(key=lambda x: (x[0], -x[1]))
#     # print(n_info)
#     # A = B = 0
#     # for a, b in n_info:
#     #     if A + a < n:
#     #         A += a
#     #     elif B + b < m:
#     #         B += b
#     #     else:
#     #         return -1
    
#     return min_A if min_A != 121 else -1

    dp = {}
    def dfs(idx, A, B):
        nonlocal dp
        
        if A >= n or B >= m:
            return 121
        if idx == len(info):
            return A
        
        key = (idx, A, B)
        if dp.get(key):
            return dp[key]
        
        cur_A, cur_B = info[idx]
        pick_A = dfs(idx+1, A+cur_A, B)
        pick_B = dfs(idx+1, A, B+cur_B)
        
        min_A = min(pick_A, pick_B)
        dp[key] = min_A
        
        # print(dp)
        
        return min_A
        
    min_A = dfs(0, 0, 0)
    
    return min_A if min_A != 121 else -1
            