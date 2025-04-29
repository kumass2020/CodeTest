from collections import deque
def solution(maps):
    answer = []
    
    M = len(maps)
    N = len(maps[0])
    visited = [[False] * N for _ in range(M)]
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(M):
        for j in range(N):
            if maps[i][j] != 'X' and not visited[i][j]:
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                summ = 0
                
                while q:
                    x, y = q.popleft()
                    summ += int(maps[x][y])
                    
                    for move in moves:
                        nx = x + move[0]
                        ny = y + move[1]
                        
                        if 0 <= nx <= M-1 and 0 <= ny <= N-1 and maps[nx][ny] != 'X' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                
                answer.append(summ)
                
    
    return sorted(answer) if answer else [-1]