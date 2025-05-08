class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        # half = N // 2
        # visited = [[False] * N for i in range(N)]

        # # for i in range(half):
        # #     for m in range(N):
        # #         for n in range(N):

        # #     temp = matrix[N-i]
        # #     matrix[N-i] = matrix[i]

        # for i in range(N):
        #     for j in range(N):
        #         rev_i, rev_j = N-i, N-j
        #         len_i, len_j = abs(i-rev_i), abs(j-rev_j)
        #         move = len_i-1

        #         x, y = i, j
        #         while x > 0 and move > 0:
        #             x -= 0

        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(N):
            matrix[i].reverse()

        







