class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])

        zeros = []
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        for i, j in zeros:
            for m in range(M):
                matrix[m][j] = 0

            for n in range(N):
                matrix[i][n] = 0
                
        # visited = [[False] * N for _ in range(M)]

        # for i in range(M):
        #     for j in range(N):
        #         if matrix[i][j] == 0 and not visited[i][j]:
        #             for m in range(M):
        #                 if matrix[m][j] != 0:
        #                     visited[m][j] = True
        #                 matrix[m][j] = 0


        #             for n in range(N):
        #                 if matrix[i][n] != 0:
        #                     visited[i][n] = True
        #                 matrix[i][n] = 0
