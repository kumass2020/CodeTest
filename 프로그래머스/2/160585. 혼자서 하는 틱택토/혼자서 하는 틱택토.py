def solution(board):
    # answer = -1
    
    N = M = 3
    
    x_count = o_count = 0
    # bingo_rows = [False] * 3
    # bingo_cols = [False] * 3
    # bingo_rows = {}
    bingo_cols = {}
    bingo_diag = {}
    for i in range(M):
        for j in range(N):
            # x, o 갯수 카운팅
            if board[i][j] == 'X':
                x_count += 1
            elif board[i][j] == 'O':
                o_count += 1
                
            # 이미 게임 끝났는데 더 하면 안됨
            # 열
            bingo_cols[j] = bingo_cols.get(j, '') + board[i][j]
            
            if i == j:
                bingo_diag[0] = bingo_diag.get(0, '') + board[i][j]
            if i+j == 2:
                bingo_diag[1] = bingo_diag.get(1, '') + board[i][j]
            
    # 후공 먼저면 안됨
    if not (x_count == o_count or x_count+1 == o_count):
        return 0

    # # 선후공 갯수 2 이상 차이 나면 안됨
    # if o_count - x_count >= 2:
    #     return 0
            
    # return 1
    
    bingo_o = 0
    bingo_x = 0
    for i in range(3):
        if board[i] == 'OOO' or bingo_cols[i] == 'OOO':
            bingo_o += 1
        elif board[i] == 'XXX' or bingo_cols[i] == 'XXX':
            bingo_x += 1
    
    for i in range(2):
        if bingo_diag[i] == 'OOO':
            bingo_o += 1
        elif bingo_diag[i] == 'XXX':
            bingo_x += 1
        
    # 선공이 마지막인데 후공 승
    # 후공이 마지막인데 선공 승
    if (bingo_o and bingo_x) or (o_count > x_count and bingo_x) or (o_count == x_count and bingo_o):
        return 0
        
    return 1


            # 열
            
    
    # return answer