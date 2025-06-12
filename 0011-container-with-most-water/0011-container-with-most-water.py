class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)

        left = 0
        right = N-1
        # height_left = -1
        # height_right = -1
        answer = -1
        while left < right:
            
            area = (right-left)*min(height[left], height[right])
            answer = max(answer, area)

            # height_left = max(height_left, height[left])
            # height_right = max(height_right, height[right])

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return answer

        # max1 = []
        # max2 = []
        # maxx = -1
        # for i in range(N):
        #     if height[i] > maxx:
        #         max1.append((i, height[i]))
        #         maxx = height[i]

        # maxx = -1
        # for j in range(N-1, -1, -1):
        #     if height[j] > maxx:
        #         max2.append((j, height[j]))
        
        # answer = -1
        # for i, height_i in max1:
        #     for j, height_j in max2:
        #         if j > i:
        #             answer = max(answer, (j-i)*min(height_i, height_j))
        
        # return answer
