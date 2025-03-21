# # def solution(places):
# #     answer = []
    
# #     seat_to_check = []
# #     for i in range(-2, 3):
# #         for j in range(-2, 3):
# #             if abs(i) + abs(j) <= 2 and (i != 0 or j != 0):
# #                 seat_to_check.append((i, j))
    
    
# #     for place in places:
# #         counter = 0
# #         for i, row in enumerate(place):
# #             for j, elem in enumerate(row):
# #                 if counter == 0:
# #                     if place[i][j] == "P":
# #                         for move in seat_to_check:
# #                             x = i + move[0]
# #                             y = j + move[1]

# #                             if (0 <= x <= 4) and (0 <= y <= 4) and place[x][y] == "P":
# #                                 if abs(i-x) == 2:
# #                                     if place[i + move[0]//2][y] == "X":
# #                                         pass
# #                                     else:
# #                                         answer.append(0)
# #                                         counter += 1
# #                                         break
# #                                 elif abs(j-y) == 2:
# #                                     if place[x][j + move[1]//2] == "X":
# #                                         pass
# #                                     else:
# #                                         answer.append(0)
# #                                         counter += 1
# #                                         break
# #                                 elif abs(i-x) == 1 and abs(j-y) == 1:
# #                                     if place[i][y] == "X" and place[x][j] == "X":
# #                                         pass
# #                                     else:
# #                                         answer.append(0)
# #                                         counter += 1
# #                                         break
# #                                 else:       
# #                                     answer.append(0)
# #                                     counter += 1
# #                                     break
                                
# #                 else:
# #                     break
                
# #         if not counter:
# #             answer.append(1)
                                
                
                            
                    
    
# #     return answer

# from collections import deque

# def is_safe(place):
#     directions = [(-1,0),(1,0),(0,-1),(0,1)]  # only up, down, left, right
    
#     for r in range(5):
#         for c in range(5):
#             if place[r][c] == 'P':
#                 visited = [[0]*5 for _ in range(5)]
#                 queue = deque([(r,c,0)])
#                 visited[r][c] = 1
                
#                 while queue:
#                     x,y,dist = queue.popleft()
#                     if dist >= 2:
#                         continue
#                     for dx,dy in directions:
#                         nx, ny = x+dx, y+dy
#                         if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
#                             visited[nx][ny] = 1
#                             if place[nx][ny] == 'O':
#                                 queue.append((nx,ny,dist+1))
#                             # Person found within distance and no partition
#                             if place[nx][ny] == 'P':
#                                 return False
#     return True

# def solution(places):
#     return [1 if is_safe(place) else 0 for place in places]


from collections import deque

def solution(places):
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    answer = []
    
    def dfs(place):
        for i in range(5):
            for j in range(5):

                if place[i][j] == 'P':
                    q = deque()
                    q.append((i, j, 0))
                    visited = [[0] * 5 for _ in range(5)]
                    visited[i][j] = 1

                    while q:
                        cx, cy, dist = q.popleft()

                        if dist > 2:
                            continue

                        if place[cx][cy] == 'P' and visited[cx][cy] == 0:
                            return 0

                        visited[cx][cy] = 1


                        for move in moves:
                            x = cx + move[0]
                            y = cy + move[1]

                            if 0 <= x <= 4 and 0 <= y <= 4 and place[x][y] != 'X' and not visited[x][y]:
                                q.append((x,y,dist+1))

                    
        
        return 1
    
    for place in places:
        answer.append(dfs(place))
    
    return answer






















