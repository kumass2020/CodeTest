class Solution:
    def trailingZeroes(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n <= 4:
        #     return 0
        
        # num = 1
        # count = 0
        # for i in range(1, n+1):
        #     num *= i

        #     while num % 10 == 0:
        #         count += 1
        #         num //= 10
        
        # return count

        # count = 0
        # for i in range(5, n+1, 5):
        #     count += 1

        #     for j in [5, 4, 3, 2]:
        #         if i % 5**j == 0:
        #             count += j-1
        #             break

        # return count

        def get_zero(n):
            if n <= 4:
                return 0
            exp = 0
            coeff = 0
            for i in range(6):
                if 5**i <= n < 5**(i+1):
                    exp = i
                    coeff = n // (5**i)

            # print(n, exp, coeff)
            count = 0
            for i in range(exp):
                count += coeff * (5**i)

                if i == exp-1:
                    # count += (n - coeff*(5**i)) // 5
                    count += get_zero(n - coeff*(5**(i+1)))
        
            return count
        return get_zero(n)