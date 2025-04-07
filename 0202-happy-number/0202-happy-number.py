class Solution:
    def isHappy(self, n: int) -> bool:
        n_buffer = n
        while True:
            num = 0
            while n != 0:
                num += (n % 10)**2
                n //= 10
            print(num)
            if num == 1:
                return True
            else:
                if num == 20:
                    return False

                n = num

        
        # if cycle, false