class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # c = str(int(a) + int(b))
        # answer = ''
        # for i in range(len(c), -1, -1):
        #     if c[i] ==
        #     answer = c[i] + answer 

        def get_10(binary):
            j = 0
            num = 0
            for i in range(len(binary)-1, -1, -1):
                num += int(binary[i]) * (2**(j))
                j += 1
            return num
        
        def get_2(num):
            answer = ''
            while num > 0:
                answer = str(num % 2) + answer
                num = num // 2
            return answer if answer else '0'

        a = get_10(a)
        b = get_10(b)

        return get_2(a + b)
