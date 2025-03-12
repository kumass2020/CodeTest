# def solution(edges):
#     answer = [0 for i in range(4)]
#     relations = {}  # relations[num] = [[in], [out]]
    
#     for edge in edges:
#         start = edge[0]
#         end = edge[1]
        
#         if relations.get(start):
#             relations[start][1].append(end)
#         else:
#             relations[start] = [[], [end]] 
        
#         if relations.get(end):
#             relations[end][0].append(start)
#         else:
#             relations[end] = [[start], []]
        
#         # if edge[0] == edge[1]:
#             # answer[1] += 1
    
#     for i in range(1, max(relations.keys())+1):
#         key = i
#         if relations.get(key):
#             value = relations[key]

#             if len(value[1]) > 2:
#                 answer[0] = key
#             elif len(value[1]) == 2:    # 8자 혹은 추가 정점
#                 if len(value[0]) == 0:  # 추가된 정점
#                     answer[0] = key

#             connections = 0
#             # nodes = [key]
#             # current_node = value
#             nodes = stack = [key]
#             is_eight = False
#             is_bar = False
#             while stack:
#                 current_node = stack.pop()
                
#                 _in = relations[current_node][0]
#                 out = relations[current_node][1]
                
#                 # 만약 특정 노드에 input >= 2, output >= 2
#                 if len(_in) >= 2 and len(out) >= 2:
#                     is_eight = True
#                 elif len(out) == 0:
#                     is_bar = True
                
#                 if _in and out and _in[0] == out[0]:
#                     break
                
#                 if current_node in nodes:
#                     break

#                 for elem in out:
#                     stack.append(elem)

#                 nodes.append(current_node)
#                 connections += 1
            
#             if is_bar:
#                 answer[2] += 1
#             elif is_eight:
#                 answer[3] += 1
#             else:
#                 answer[1] += 1
                
#             for node in nodes:  # dictionary clearance
#                 relations.pop(node) if relations.get(node) else 1
            
            
    
#     return answer

from collections import defaultdict, deque

def solution(edges):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    adj = defaultdict(list)
    vertices = set()
    
    for u, v in edges:
        outdegree[u] += 1
        indegree[v] += 1
        
        adj[u].append(v)
        adj[v].append(u)
        vertices.add(u)
        vertices.add(v)
    
    extra = None
    for v in vertices:
        if indegree[v] == 0 and outdegree[v] >= 2:
            extra = v
            break
    if extra is None:
        return []
    
    vertices.remove(extra)
    for neighbor in adj[extra]:
        if extra in adj[neighbor]:
            adj[neighbor].remove(extra)
    del adj[extra]
    
    visited = set()
    donut_count = 0
    bar_count = 0
    eight_count = 0
    
    for v in vertices:
        if v not in visited:
            comp_vertices = []
            comp_edges = 0
            q = deque([v])
            visited.add(v)
            while q:
                curr = q.popleft()
                comp_vertices.append(curr)
                for nb in adj[curr]:
                    comp_edges += 1
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            
            comp_edges //= 2
            
            if comp_edges == len(comp_vertices):
                donut_count += 1
            elif comp_edges == len(comp_vertices) - 1:
                bar_count += 1
            elif comp_edges == len(comp_vertices) + 1:
                eight_count += 1
    return [extra, donut_count, bar_count, eight_count]