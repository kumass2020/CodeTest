# def solution(n, tops):
#     answer = 0
#     edges = [0 for i in range(2*n)]
#     visited = [0 for i in range(2*n+1)]
    
#     for i, top in enumerate(tops):
#         for j in range(top+1):
#             if j == 0: # 윗 삼각형 x
#                 for k in range(2):
#                     if k == 0:
                        
#             if j == 1: # 윗 삼각형 o
#                 for k in range(3):
#                     if k == 0:  # 안칠함
#                         pass
#                     elif k == 1: # 다음 노드랑 연결
#                         edges[i] = 1
#                         visited[i] = visited[i+1] = 1
#                     elif k == 2: # 윗 노드랑 연결
#                         visited[i] = 1
#                     visited[]
        
    
#     return answer

def solution(n, tops):
    # n_case = 
    a = [0] * n
    b = [0] * n
    a[0] = 1   # 침범
    b[0] = 3 if tops[0] == 1 else 2    # 침범 x
    for i in range(1, n):
        if tops[i] == 1:
            a[i] = (a[i-1] + b[i-1]) % 10007
            b[i] = (2 * a[i-1] + 3 * b[i-1]) % 10007
        else:
            a[i] = (a[i-1] + b[i-1]) % 10007
            b[i] = (a[i-1] + 2 * b[i-1]) % 10007
    
    return (a[-1] + b[-1]) % 10007
        
        
        
        