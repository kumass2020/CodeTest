class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        # return int(str(n)[::-1])
        # for i in range(len(n)-1, -1, -1):
        #     j = 0
        #     if n[i] == '1':
        #         answer += (2**j)

        #     j += 1
        
        # return answer

        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result |= (bit << (31-i))
        
        return result