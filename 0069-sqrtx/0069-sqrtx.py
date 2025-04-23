class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        for i in range(x):
            if i*i > x:
                num = i-1
                break 
        if 1 <= x <= 3:
            return 1 
        return num 