class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])

        answer = []
        # for i in range(N):
        #     answer.append(matrix[0][i])
        
        visited = [[False] * N for _ in range(M)]

        # moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        moves = ['r', 'd', 'l', 'u', 'r']

        def traverse(i, j, d):
            if len(answer) == M*N:
                return
            if not visited[i][j]:
                answer.append(matrix[i][j])
                # return
            visited[i][j] = True
            
            orig_i = i
            orig_j = j
            
            if d == 'r':
                j += 1
            elif d == 'd':
                i += 1
            elif d == 'l':
                j -= 1
            elif d == 'u':
                i -= 1
            
            if 0 <= i <= M-1 and 0 <= j <= N-1 and not visited[i][j]:
                traverse(i, j, d)
            else:
                traverse(orig_i, orig_j, moves[moves.index(d)+1])
        
        traverse(0, 0, 'r')
        return answer