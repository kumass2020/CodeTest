class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if 0 <= x <= 9:
        #     return True
        # elif x < 0:
        #     return False
        
        # orig_x = x
        # num = 0
        # i = 0
        # # while x != 0:
        # #     # print((10**i) * (x % 10))
        # #     # num += (10**i) * (x % 10)
        # #     num.append(str(x % 10))
        # #     x //= 10
        # #     i += 1
        
        # return orig_x == int(''.join(num))

        if x < 0:
            return False
        
        x_cp = x
        num = 0
        # i = 0
        while x_cp != 0:
            # print(10 * num, x_cp % 10)
            num = 10 * num + x_cp % 10
            x_cp //= 10
        
        return x == num
