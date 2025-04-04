class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        i = 0
        j = 0
        while i <= len(nums)-1:
            j += 1
            
            while j <= len(nums)-1 and nums[j] - nums[j-1] == 1:
                j += 1
            
            if i == j-1:
                answer.append(f"{nums[i]}")
            else:
                answer.append(f"{nums[i]}->{nums[j-1]}")
            # print(answer, i, j)
            i = j

            if j == len(nums)-1:
                if nums[j] - nums[j-1] != 1:
                    answer.append(f"{nums[j]}")
                return answer

        return answer