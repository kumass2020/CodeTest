# from collections import deque

# def solution(board):
#     # answer = 0
    
#     r = len(board)
#     c = len(board[0])
    
#     dist_mat = [[-1] * c for _ in range(r)]
    
#     queue = deque()
    
#     for row in range(r):
#         for col in range(c):
#             if board[row][col] == 'R':
#                 cpos = (row, col)
#                 dist_mat[row][col] = 0
    
#     queue.append(cpos)
    
#     moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     def get_moved_pos(cpos):
#         moved_pos = []
#         for move in moves:
#             pos = cpos
#             counter = 0
#             while True:
#                 counter += 1
#                 # pos = pos + move
#                 row = pos[0] + move[0]
#                 col = pos[1] + move[1]
                
#                 if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1:
#                     break
    
#                 if board[row][col] == 'D':
#                     if counter > 1:
#                         moved_pos.append((row-move[0], col-move[1]))
#                         break
#                     else:
#                         break
                    
#                 if move == (-1, 0) and row == 0:
#                     moved_pos.append(pos)
#                     break
#                 elif move == (1, 0) and row == len(board)-1:
#                     moved_pos.append(pos)
#                     break
#                 elif move == (0, -1) and col == 0:
#                     moved_pos.append(pos)
#                     break
#                 elif move == (0, 1) and col == len(board[0])-1:
#                     moved_pos.append(pos)
#                     break
        
#         return moved_pos
                
#     while queue:
#         cpos = queue.popleft()
#         crow = cpos[0]
#         ccol = cpos[1]
#         cdist = dist_mat[crow][ccol]
        
#         for pos in get_moved_pos(cpos):
#             row = pos[0]
#             col = pos[1]
#             if dist_mat[row][col] == -1:
#                 dist_mat[row][col] = cdist+1
#                 queue.append((row, col))
    
#     for row in range(r):
#         for col in range(c):
#             if board[row][col] == 'G':
#                 goal_pos = (row, col)
    
#     g_row = goal_pos[0]
#     g_col = goal_pos[1]
    
#     if dist_mat[g_row][g_col] == -1:
#         return -1
#     else:
#         return dist_mat[g_row][g_col]
            
            
#     # return answer

from collections import deque

def solution(board):
    R = len(board)
    C = len(board[0])
    
    start = None
    goal = None
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    
    dist = [[-1] * C for _ in range(R)]
    dist[start[0]][start[1]] = 0
         
    q = deque([start])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def slide(pos, d):
        i, j = pos
        di, dj = d
        
        while True:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= R or nj < 0 or nj >= C or board[ni][nj] == 'D':
                return (i, j)
            i, j = ni, nj
    
    while q:
        cur = q.popleft()
        if cur == goal:
            return dist[cur[0]][cur[1]]
        for d in directions:
            nxt = slide(cur, d)
            if dist[nxt[0]][nxt[1]] == -1:
                dist[nxt[0]][nxt[1]] = dist[cur[0]][cur[1]] + 1
                q.append(nxt)
        
    return -1
    
    
         
         

    