from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])

        moves = [(-1,0), (0, -1), (1, 0), (0, 1)]

        # O_lst = []
        visited = [[False] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O' and not visited[i][j]:
                    q = deque()
                    q.append((i, j))
                    history = []
                    
                    while q:
                        x, y = q.popleft()
                        # print(x, y)
                        
                        if x == 0 or x == M-1 or y == 0 or y == N-1:
                            history = []
                            # print(history)
                            break

                        visited[x][y] = True
                        history.append((x, y))

                        for move in moves:
                            nx = x + move[0]
                            ny = y + move[1]

                            # print("nx, ny:", nx, ny)

                            if 0 <= nx <= M-1 and 0 <= ny <= N-1 and board[nx][ny] == 'O' and not visited[nx][ny]:
                                q.append((nx, ny))
                    # print(history)
                    for x,y in history:
                        board[x][y] = 'X'
                    # O_lst.extend()
            
        # for x,y in O_lst:
            


