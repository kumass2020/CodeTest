def solution(board, skill):
    answer = 0
    
#     for s in skill:
#         _type, r1, c1, r2, c2, degree = s
        
#         coeff = -1 if _type == 1 else 1
        
#         for row in range(r1, r2+1):
#             for col in range(c1, c2+1):
#                 board[row][col] += coeff * degree
        
#     for r in board:
#         for elem in r:
#             if elem >= 1:
#                 answer += 1

    N = len(board)
    M = len(board[0])
    
    matrix = [[0] * (M+1) for i in range(N+1)]
    for s in skill:
        _type, r1, c1, r2, c2, degree = s
        coeff = -1 if _type == 1 else 1
        degree = coeff * degree
        
        matrix[r1][c1] += degree
        matrix[r1][c2+1] -= degree
        matrix[r2+1][c1] -= degree
        matrix[r2+1][c2+1] += degree
        
    for row in range(N):
        for col in range(1, M):
            matrix[row][col] += matrix[row][col-1]
              
    for col in range(M):
        for row in range(1, N):
            matrix[row][col] += matrix[row-1][col]
    
    # board += matrix
    
#     for row in range(N):
#         for col in range(M):
#             elem = board[row][col] + matrix[row][col]
#             if elem >= 1:
#                 answer += 1
    
#     return answer
    return sum(board[r][c] + matrix[r][c] > 0 for r in range(N) for c in range(M))