class Solution:
    def hammingWeight(self, n: int) -> int:
        
        i = 0
        count = 0
        while n != 0:
            res = n % 2
            count += res
            # count += (res >> i) & 1
            n //= 2
            i += 1

        return count
