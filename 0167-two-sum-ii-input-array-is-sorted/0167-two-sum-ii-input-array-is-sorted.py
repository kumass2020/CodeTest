class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        i = 0
        j = N-1

        for i in range(N):
            num1 = numbers[i]
            num2 = target-num1

            while numbers[j] > num2:
                j -= 1 
            
            if numbers[j] == num2:
                return [i+1, j+1]
            

            
