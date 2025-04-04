class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = []
        for i, row in enumerate(matrix):
            if i >= 1 and target < row[0]:
                target_row = matrix[i-1]
                break
            elif len(matrix) == 1:
                target_row = matrix[0]
        
        if not target_row:
            target_row = matrix[-1]

        # print(target_row)
        for num in target_row:
            if num == target:
                return True
            
        return False

