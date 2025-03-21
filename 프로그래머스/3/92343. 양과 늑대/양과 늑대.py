# # from collections import deque

# # def solution(info, edges):
# #     answer = 0
    
# #     child = [[] for i in range(17)]
# #     parent = [0 for i in range(17)]
    
    
# #     for i, edge in enumerate(edges):
# #         idx = edge[0]
# #         child_num = edge[1]
        
# #         child[idx].append(child_num)
# #         parent[child_num] = idx
        
# #     # (idx, cost)
# #     q = deque()
# #     q.append((0, 0))
# #     res_sheep = 0
# #     sheep = 0
    
# #     cost = [0 for i in range(len(info))]
# #     visited = [0 for i in range(len(info))]
    
# #     while q:
# #         c_idx, res_sheep = q.popleft()
# #         # c_idx = c_info
# #         visited[c_idx] = 1
# #         cost[c_idx] = 99

# #         if info[c_idx] == 0:
# #             res_sheep += 1
# #             sheep += 1
# #         else:
# #             res_sheep -= 1

# #         # 모든 노드를 돌면서 양까지 닿는 cost를 업데이트
# #         def update_subtree(c_idx):
# #             for idx in child[c_idx]:
# #                 if info[c_idx] == 0:
# #                     cost[idx] -= 1
# #                 else:
# #                     cost[idx] += 1
# #                 update_subtree(idx)
                
# #         if len(q) == 0:
# #             min_cost = min(cost)
# #             min_cost_idx = cost.index(min_cost)

# #             idx = min_cost_idx
# #             while idx != c_idx:
# #                 if not visited[idx]:
# #                     q.appendleft((idx, res_sheep))
# #                     idx = parent[idx]
                
# # #     for i in range(0, len(info)):
# # #         parent_idx = parent[i]
# # #         j = i
# # #         res_sheep = 0
        
# # #         while True:
# # #             if j == 0:
# # #                 cost[i] = res_sheep
# # #                 break
                
# # #             if info[j] == 0:
# # #                 res_sheep += 1
# # #             else:
# # #                 res_sheep -= 1
# # #             j = parent[j]
        
# # #         if sheep <= wolf:
# # #             break
        
# # #         for idx in child[i]:
# # #             if child[idx] == 0:
# # #                 q.appendleft((idx, info[idx]))
# # #                 continue
# # #             elif child[idx] == 1:
# # #                 q.append((idx, info[idx]))
# # #                 continue
        
# #     answer = sheep
# #     return answer

# def solution(info, edges):
#     n = len(info)
#     graph = [[] for _ in range(n)]
    
#     for parent, child in edges:
#         graph[parent].append(child)
    
#     answer = 0 
    
#     def dfs(sheep, wolf, candidates):
#         nonlocal answer
        
#         answer = max(answer, sheep)
        
#         for i, node in enumerate(candidates):
#             ns, nw = sheep, wolf
#             if info[node] == 0:
#                 ns += 1
#             else:
#                 nw += 1
#             if nw >= ns:
#                 continue
                
#             new_candidates = candidates[:]
#             new_candidates.remove(node)
#             new_candidates.extend(graph[node])
            
#             dfs(ns, nw, new_candidates)
    
#     dfs(1, 0, graph[0])
#     return answer

def solution(info, edges):
    N = len(info)
    parents = [0 for i in range(N)]
    children = [[] for i in range(N)]
    
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        
        parents[child] = parent
        children[parent].append(child)
        
    answer = 0 
    
    def dfs(sheep, wolf, candidates):
        nonlocal answer
        answer = max(answer, sheep)
        
        for cand in candidates:
            new_candidates = candidates[:]
            new_sheep = sheep
            new_wolf = wolf
            
            if info[cand] == 0:
                new_sheep += 1
            else:
                new_wolf += 1
            
            if new_wolf >= new_sheep:
                continue
                
            new_candidates.extend(children[cand])
            new_candidates.remove(cand)
            
            dfs(new_sheep, new_wolf, new_candidates)
        
        return answer
    
    answer = dfs(0, 0, [0])
    
    return answer
            
            
        
        
        
        
        