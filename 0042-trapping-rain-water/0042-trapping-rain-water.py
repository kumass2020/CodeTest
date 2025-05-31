class Solution:
    def trap(self, height: List[int]) -> int:
        H = max(height)
        N = len(height)

        left_max = [0] * N
        right_max = [0] * N
        left_max[0] = height[0]
        right_max[N-1] = height[N-1]
        for i in range(1, N):
            left_max[i] = max(left_max[i-1], height[i])
        
        for i in range(N-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        answer = 0
        for i in range(N):
            # print(max(min(left_max[i], right_max[i]) - height[i], 0))
            answer += max(min(left_max[i], right_max[i]) - height[i], 0)
        
        return answer

        # # matrix (elevation map) 구성
        # # matrix

        # # row 마다, 검은색 시작 - 검은색 끝인 영역 세기 
        # answer = 0
        # # visited = [[False] * N for _ in range(H)]
        # # visited2 = [[False] * N for _ in range(H)]
        # visited = set()
        # visited2 = set()
        # for i in range(1, N):
        #     # print(buffer)
        #     if height[i] < height[i-1]:
        #         j = i
        #         while j < N:
        #             # print(height[i-1], height[j])
        #             if height[i-1] > height[j]:
        #                 # answer += (height[i-1]-height[j])
        #                 for k in range(height[j], height[i-1]):
        #                     # if not visited[k][j]:
        #                     if (k, j) not in visited:
        #                         # print(j, k)
        #                         # answer += 1
        #                         # visited[k][j] = True
        #                         visited.add((k, j))
        #             elif height[i-1] <= height[j]:
        #                 break
        #             j += 1
        #         # for j in range(height[i], height[i-1]):
        #         #     buffer[j] += 1

        # for i in range(N-2, -1, -1):
        #     # print(buffer)
        #     if height[i] < height[i+1]:
        #         j = i
        #         while j > 0:
        #             # print(height[i-1], height[j])
        #             if height[i+1] > height[j]:
        #                 # answer += (height[i-1]-height[j])
        #                 for k in range(height[j], height[i+1]):
        #                     # if not visited2[k][j] and visited[k][j]:
        #                     if (k, j) not in visited2 and (k, j) in visited:
        #                         # print(j, k)
        #                         answer += 1
        #                         # visited2[k][j] = True
        #                         visited2.add((k, j))
        #             elif height[i+1] <= height[j]:
        #                 break
        #             j -= 1
                
        #     # if height[i] > height[i-1]:
        #     #     for j in range(height[i-1], height[i]):
        #     #         answer += buffer[j]
        #     #         buffer[j] = 0

        # return answer


