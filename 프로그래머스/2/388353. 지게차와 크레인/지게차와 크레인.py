from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    # grid: container letter 혹은 제거된 곳은 '.'으로 표시
    grid = [list(row) for row in storage]
    
    # 외부와 연결된(즉, 외부에서 도달 가능한) 빈 칸을 찾는 BFS 함수
    def get_reachable_empty():
        visited = [[False]*m for _ in range(n)]
        dq = deque()
        # 먼저, 경계에 위치하면서 이미 빈 칸인 곳을 시작점으로 추가합니다.
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == '.':
                    visited[i][j] = True
                    dq.append((i, j))
        # BFS 수행: 빈 칸만 이동할 수 있습니다.
        while dq:
            i, j = dq.popleft()
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == '.' and not visited[ni][nj]:
                        visited[ni][nj] = True
                        dq.append((ni, nj))
        return visited

    # 각 출고 요청을 순서대로 처리합니다.
    for req in requests:
        target = req[0]
        if len(req) == 2:
            # 크레인 요청: 요청한 종류의 모든 컨테이너 제거
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        grid[i][j] = '.'
        else:
            # 지게차 요청: "접근 가능한" 컨테이너만 제거
            reachable = get_reachable_empty()  # 외부와 연결된 빈 칸 표시
            removal = []  # 제거할 컨테이너의 좌표들
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == target:
                        # 경계에 있으면 바로 접근 가능
                        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                            removal.append((i, j))
                        else:
                            # 인접 4방향 중 하나라도 빈 칸이면서 외부와 연결되어 있으면 접근 가능
                            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                                ni, nj = i + di, j + dj
                                if grid[ni][nj] == '.' and reachable[ni][nj]:
                                    removal.append((i, j))
                                    break
            # 동시에 제거 처리
            for i, j in removal:
                grid[i][j] = '.'
                
    # 모든 요청을 처리한 후 남은 컨테이너의 수를 계산
    answer = sum(cell != '.' for row in grid for cell in row)
    return answer
