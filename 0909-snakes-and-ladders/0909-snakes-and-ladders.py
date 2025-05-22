from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)

        board = [board[i][j] for i in reversed(range(N)) for j in (range(N) if (N-i) % 2 == 1 else reversed(range(N)))]
        # print(board)

        q = deque()
        q.append((1, 0))
        # visited = [False] * (N**2)
        visited = set()
        # move = 0
        while q:
            curr, move = q.popleft()
            # move += 1
            # visited[curr-1] = True
            visited.add(curr-1)

            if curr == N*N:
                return move

            i = curr+1
            j = min(curr+6, N**2)+1

            for square_num in range(i, j):
                if board[square_num-1] != -1:
                    _next = board[square_num-1]
                else:
                    _next = square_num
                
                # if not visited[_next-1]:
                if not _next-1 in visited:
                    q.append((_next, move+1))
        
        return -1


        # # i, j = square_num // N, square_num % N
        # # print(board)
        # move = i = j = 0
        # curr = 1
        # visited = [False] * (N**2)
        # while curr != N**2:
        #     if visited[curr-1]:
        #         return -1

        #     move += 1
        #     visited[curr-1] = True

        #     if curr+6 >= N**2:
        #         return move

        #     i = curr+1
        #     j = min(curr+6, N**2)+1

        #     # print(curr)
        #     for square_num in range(i, j):
        #         # print(square_num)
        #         if board[square_num-1] != -1:
        #             curr = board[square_num-1]
        #             break
        #         elif square_num == j-1:
        #             curr = square_num

        #         # i, j = square_num // N, square_num % N
        #         # print(i, j)
        #         # if not board[i][j]:
        #         #     curr = board[i][j]
        #         #     break
        #         # elif square_num == min(curr+6, N**2):
        #         #     curr = square_num

        # return move
            
