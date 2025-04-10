class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                
        M = len(board)
        N = len(board[0])

        for row in board:
            lst = []
            for elem in row:
                if elem == '.' or elem not in lst:
                    lst.append(elem)
                else:
                    return False

        for i in range(M):
            lst = []
            for j in range(N):
                elem = board[j][i]
                if elem == '.' or elem not in lst:
                    lst.append(elem)
                else:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                lst = []
                for k in [0,1,2]:
                    for l in [0,1,2]:
                        elem = board[i+k][j+l]
                        if elem == '.' or elem not in lst:
                            lst.append(elem)
                        else:
                            return False

        return True