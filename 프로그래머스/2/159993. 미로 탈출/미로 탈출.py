# def solution(maps):
#     answer = 0
    
#     def find_idx_2d(matrix, value):
#         for r, row in enumerate(matrix):
#             if value in row:
#                 return r, row.index(value)
#         return None
    
#     start_idx = find_idx_2d(maps, 'S')
#     lever_idx = find_idx_2d(maps, 'L')
#     end_idx = find_idx_2d(maps, 'E')
    
#     idxs = (start_idx, lever_idx, end_idx)
    
#     moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
#     current_pos = [start_idx]
    
#     # 레버
#     while True:
        
        
    
#     # exit
#     while True:
        
        
        
    
#     return answer


# from collections import deque

# def solution(maps):
#     # Get dimensions of map
#     rows = len(maps)
#     cols = len(maps[0])
    
#     # Find Start, Lever, End
#     start = lever = exit_point = None
#     for i in range(rows):
#         for j in range(cols):
#             if maps[i][j] == 'S':
#                 start = (i, j)
#             elif maps[i][j] == 'L':
#                 lever = (i, j)
#             elif maps[i][j] == 'E':
#                 exit_point = (i, j)
                
#     def bfs(start, target):
#         # -1로 distance grid 초기화
#         distances = [[-1] * cols for _ in range(rows)]
#         queue = deque()
        
#         # 시작점부터
#         sx, sy = start
#         distances[sx][sy] = 0
#         queue.append((sx, sy))
        
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
#         while queue:
#             x, y = queue.popleft()
            
#             # target에 도달하면 distance return
#             if maps[x][y] == target:
#                 return distances[x][y]
            
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
                
#                 # 현재 위치가 map 안이면
#                 if 0 <= nx < rows and 0 <= ny < cols:
#                     # wall이 아니면서 아직 방문하지 않은 곳이면
#                     if maps[nx][ny] != 'X' and distances[nx][ny] == -1:
#                         distances[nx][ny] = distances[x][y] + 1
#                         queue.append((nx, ny))
#         return -1   # target에 못가는 경우
    
#     # Start -> Lever
#     distance_SL = bfs(start, 'L')
#     if distance_SL == -1:
#         return -1
    
#     distance_LE = bfs(lever, 'E')
#     if distance_LE == -1:
#         return -1
    
#     return distance_SL + distance_LE
    
    
from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    start = lever = end = None
    
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    
    # x = y = None
    # cx = start[0]
    # cy = start[1]
    
    # sx = sy = 0
    
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    def bfs(start, target):
        queue = deque()
        
        sx = start[0]
        sy = start[1]
        
        queue.append((sx, sy))
            
        dist_mat = [[-1] * cols for i in range(rows)]
        dist_mat[start[0]][start[1]] = 0
    
        while queue:
            cx, cy = queue.popleft()
            # current_pos = (cx, cy)

            if maps[cx][cy] == target:
                return dist_mat[cx][cy]

            for move in moves:
                x = cx + move[0]
                y = cy + move[1]

                if 0 <= x <= rows-1 and 0 <= y <= cols-1:
                    if maps[x][y] != 'X' and dist_mat[x][y] == -1:
                        dist_mat[x][y] = dist_mat[cx][cy] + 1
                        queue.append((x, y))
        
        return -1
    
    dist_SL = bfs(start, 'L')
    
    if dist_SL == -1:
        return -1
    
    dist_LE = bfs(lever, 'E')
    
    if dist_LE == -1:
        return -1
    
    return dist_SL + dist_LE
                    
                    
                
            

        