# from collections import deque

# def bfs(land, starting_point):
#     # cx, cy = starting_point
    
#     queue = deque()
#     queue.append(starting_point)
    
#     moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
#     area = 0
    
#     while queue:
#         area += 1
#         cx, cy = queue.popleft()
#         for move in moves:
#             x = cx + move[0]
#             y = cy + move[1]
            
#             if 0 <= x <= len(land)-1 and 0 <= y <= len(land[0])-1:
#                 if land[x][y] == 1:
#                     queue.append((x,y))
    
#     return area
                    
    

# def solution(land):
#     # answer = 0
#     total_area = 0
    
#     for i in range(len(land[0])):
#         for j in range(len(land)):
#             if land[j][i] == 1:
#                 if j-1 > 0 and land[j-1][i]:
#                     continue
#                 # if j+1 < len(land) and land[j+1][i]:
#                     # continue
#                 total_area += bfs(land, (j, i))
    
#     return total_area

from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    cluster_id = [[0] * m for _ in range(n)]
    cluster_size = {}
    id_counter = 1
    
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and cluster_id[i][j] == 0:
                queue = deque([(i, j)])
                cluster_id[i][j] = id_counter
                size = 0
                
                while queue:
                    x, y = queue.popleft()
                    size += 1
                    for dx, dy in moves:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and cluster_id[nx][ny] == 0:
                                cluster_id[nx][ny] = id_counter
                                queue.append((nx, ny))
                
                cluster_size[id_counter] = size
                id_counter += 1
                
    max_oil = 0
    for col in range(m):
        clusters_in_column = set()
        for row in range(n):
            cid = cluster_id[row][col]
            if cid != 0:
                clusters_in_column.add(cid)
        oil = sum(cluster_size[cid] for cid in clusters_in_column)
        max_oil = max(max_oil, oil)
        
    return max_oil