# def solution(n, m, x, y, r, c, k):
#     answer = ''
    
#     # dlru
#     moves_str = 'dlru'
#     moves = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    
#     # 일단 최소 거리부터 찾기
#     def get_distance(x, y):
#         return abs(x-r) + abs(y-c)
    
#     distance = get_distance(x, y)
    
#     # 거리는 최소 거리 + 2n만 가능함
#     if k - distance < 0 or (k - distance) % 2 == 1:
#         return 'impossible' 

#     # 최소로 가는 경로를 사전 순으로 빠르게 정하기
#     move = 0
#     cx = x
#     cy = y
#     while 1 <= cx < n and get_distance(cx, cy) != k-move:
#         answer += 'd'
#         move += 1
#         cx += 1
    
#     while 1 < cy <= m and get_distance(cx, cy) != k-move:
#         answer += 'l'
#         move += 1
#         cy -= 1
    
#     while 1 <= cy < m and get_distance(cx, cy) != k-move:
#         answer += 'r'
#         move += 1
#         cy += 1
    
#     while 1 < cx <= n and get_distance(cx, cy) != k-move:
#         answer += 'u'
#         move += 1
#         cx -= 1
        
#     new_dist = 2501
#     while new_dist:
#         for i, _move in enumerate(moves):
#             x = cx + _move[0]
#             y = cy + _move[1]
            
#             cdistance = get_distance(cx, cy)
#             new_dist = get_distance(x, y)
            
#             if 1 <= x <= n and 1 <= y <= m and cdistance > new_dist:
#                 answer += moves_str[i]
#                 move += 1
#                 cx = x
#                 cy = y
                
#                 break
            
                
                
                
        
    
#     # 벽 조심
    
    
    
# #     # 2n은 du, rl, lr, ud 순
# #     p = (k - move) // 2
# #     if r <= n-1:
# #         answer += 'du' * p
# #         move += 2 * p
    
# #     elif c <= m-1:
# #         answer += 'rl' * p
# #         move += 2 * p
    
# #     elif c >= 1:
# #         answer += 'lr' * p
# #         move += 2 * p
    
# #     elif r >= 1:
# #         answer += 'ud' * p
# #         move += 2 * p
    
#     # if k-move-p*2 != 0:
#     #     return 'impossible'
    
#     return answer

def solution(n, m, x, y, r, c, k):
    # 0 index로
    x, y, r, c = x-1, y-1, r-1, c-1
    
    def manhattan(ax, ay, bx, by):
        return abs(ax-bx) + abs(ay-by)
    
    if manhattan(x, y, r, c) > k or (k - manhattan(x, y, r, c)) % 2 != 0:
        return "impossible"
    
    moves = [
        ('d', 1, 0),
        ('l', 0, -1),
        ('r', 0, 1),
        ('u', -1, 0)
    ]
    
    answer = []
    cur_x, cur_y = x, y
    
    for step in range(1, k+1):   # 어차피 k step 갈거임
        for letter, dx, dy in moves:
            nx, ny = cur_x + dx, cur_y + dy
            if not (0 <= nx < n and 0 <= ny < m):   # 벽이면 넘기고
                continue
            
            remaining = k - step
            
            if manhattan(nx, ny, r, c) <= remaining and (remaining - manhattan(nx, ny, r, c)) % 2 == 0:
                answer.append(letter)
                cur_x, cur_y = nx, ny
                break
        
    return "".join(answer)