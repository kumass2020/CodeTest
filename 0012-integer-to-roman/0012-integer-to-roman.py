class Solution:
    def intToRoman(self, num: int) -> str:
        # mapping = {

        # }
        answer = ''
        while num:
            if num >= 1000:
                answer += 'M'
                num -= 1000
                continue
            elif num >= 900:
                answer += 'CM'
                num -= 900
                continue
            elif num >= 500:
                answer += 'D'
                num -= 500
                continue
            elif num >= 400:
                answer += 'CD'
                num -= 400
                continue
            elif num >= 100:
                answer += 'C'
                num -= 100
                continue
            elif num >= 90:
                answer += 'XC'
                num -= 90
                continue
            elif num >= 50:
                answer += 'L'
                num -= 50
                continue
            elif num >= 40:
                answer += 'XL'
                num -= 40
                continue
            elif num >= 10:
                answer += 'X'
                num -= 10
                continue
            elif num >= 9:
                answer += 'IX'
                num -= 9
                continue
            elif num >= 5:
                answer += 'V'
                num -= 5
                continue
            elif num >= 4:
                answer += 'IV'
                num -= 4
                continue
            elif num >= 1:
                answer += 'I'
                num -= 1
                continue
        
        return answer
            
            