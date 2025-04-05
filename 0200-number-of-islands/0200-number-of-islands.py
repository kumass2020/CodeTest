from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = [[0] * N for _ in range(M)]

        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and not visited[i][j]:
                    q = deque()
                    q.append((i, j))
                    islands += 1

                    while q:
                        x, y = q.popleft()

                        for move in moves:
                            nx, ny = x+move[0], y+move[1]
                            if 0 <= nx <= M-1 and 0 <= ny <= N-1:
                                if grid[nx][ny] == '1' and not visited[nx][ny]:
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1
        
        return islands
