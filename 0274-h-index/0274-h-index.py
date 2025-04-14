class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)

        # print(citations)
        max_idx = 0
        for i in range(len(citations)):
            if i+1 <= citations[i]:
                max_idx = i+1
            else:
                break
        
        return max_idx