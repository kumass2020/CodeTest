class Solution:
    def trailingZeroes(self, n: int) -> int:
        # if n == 0:
        #     return 0
        if n <= 4:
            return 0
        
        # num = 1
        # count = 0
        # for i in range(1, n+1):
        #     num *= i

        #     while num % 10 == 0:
        #         count += 1
        #         num //= 10
        
        # return count

        count = 0
        for i in range(5, n+1, 5):
            count += 1

            for j in [5, 4, 3, 2]:
                if i % 5**j == 0:
                    count += j-1
                    break

        return count