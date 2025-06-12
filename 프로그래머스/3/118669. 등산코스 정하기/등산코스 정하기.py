# from collections import defaultdict, deque
import heapq
def solution(n, paths, gates, summits):
    
    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    gate_set = set(gates)
    summit_set = set(summits)
    
    intensity = [float('inf')] * (n+1)
    hq = []
    
    for g in gates:
        intensity[g] = 0
        heapq.heappush(hq, (0, g))
        
    while hq:
        cur_int, u = heapq.heappop(hq)
        if cur_int > intensity[u]:
            continue
        
        if u in summit_set:
            continue
        
        for v, w in graph[u]:
            cand = max(cur_int, w)
            if cand < intensity[v]:
                intensity[v] = cand
                heapq.heappush(hq, (cand, v))
        
    best = min(summits, key=lambda x: (intensity[x], x))
    return [best, intensity[best]]
    
#     dt = defaultdict(list)
    
#     for start, end, dist in paths:
#         dt[start].append((end, dist))
#         dt[end].append((start, dist))
    
#     dp = [0] * (n+1)
#     for key, value in dt.items():
#         if key in gates:
#             dp[key] = 0
#             continue
        
#         intensity = float('inf')
#         for prev, dist in value:
#             if prev in summits:
#                 continue
            
#             intensity = min(intensity, max(dp[prev], dist))
#         dp[key] = intensity
    
#     min_summit = None
#     intensity = float('inf')
#     for summit in summits:
#         if not min_summit:
#             min_summit = summit
#             intensity = dp[summit]
#         else:
#             if dp[summit] < intensity:
#                 intensity = dp[summit]
#             elif dp[summit] == intensity and summit < min_summit:
#                 min_summit = summit
#                 intensity = dp[summit]
                
#     return [min_summit, intensity]
    
#     dt = defaultdict(list)
    
#     for start, end, dist in paths:
#         dt[start].append((end, dist))
#         dt[end].append((start, dist))
    
#     summit = None
#     intensity = float('inf')
#     # answer = [None, ]
#     for gate in gates:
#         q = deque()
#         for end, dist in dt[gate]:
#             q.append((end, dist))
        
#         visited = [False] * n
#         while q:
#             pos, dist = q.popleft()
            
#             if pos in summits:
#                 if not summit:
#                     intensity = dist
#                     summit = pos
#                 else:
#                     if dist < intensity:
#                         intensity = dist
#                         summit = pos
#                     elif dist == intensity and pos < summit:
#                         summit = pos
                    
#                 continue
            
#             for end, dist in dt[pos]:
#                 if end != gate
            
    
#     return [summit, intensity]