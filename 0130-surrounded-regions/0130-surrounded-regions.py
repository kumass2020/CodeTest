# from collections import deque
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         M = len(board)
#         N = len(board[0])

#         moves = [(-1,0), (0, -1), (1, 0), (0, 1)]

#         # O_lst = []
#         visited = [[False] * N for _ in range(M)]

#         for i in range(M):
#             for j in range(N):
#                 if board[i][j] == 'O' and not visited[i][j]:
#                     q = deque()
#                     q.append((i, j))
#                     history = []
                    
#                     while q:
#                         x, y = q.popleft()
#                         # print(x, y)

#                         if visited[x][y]:
#                             continue
                        
#                         if x == 0 or x == M-1 or y == 0 or y == N-1:
#                             history = []
#                             # print(history)
#                             break

#                         visited[x][y] = True
#                         history.append((x, y))

#                         for move in moves:
#                             nx = x + move[0]
#                             ny = y + move[1]

#                             # print("nx, ny:", nx, ny)

#                             if 0 <= nx <= M-1 and 0 <= ny <= N-1 and board[nx][ny] == 'O' and not visited[nx][ny]:
#                                 q.append((nx, ny))
#                     # print(history)
#                     for x,y in history:
#                         board[x][y] = 'X'
#                     # O_lst.extend()
            
#         # for x,y in O_lst:
            


from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        # Global visited matrix to track processed cells
        global_visited = [[False] * N for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O' and not global_visited[i][j]:
                    q = deque()
                    q.append((i, j))
                    history = []
                    region_touches_edge = False
                    
                    while q:
                        x, y = q.popleft()
                        
                        if global_visited[x][y]:
                            continue
                        global_visited[x][y] = True
                        history.append((x, y))
                        
                        if x == 0 or x == M - 1 or y == 0 or y == N - 1:
                            region_touches_edge = True
                        
                        for dx, dy in moves:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 'O' and not global_visited[nx][ny]:
                                q.append((nx, ny))
                    
                    # Flip region if it doesn't touch an edge.
                    if not region_touches_edge:
                        for x, y in history:
                            board[x][y] = 'X'