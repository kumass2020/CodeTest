class Solution:
    def romanToInt(self, s: str) -> int:
        dt = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        answer = 0
        i = 0
        while i < len(s):
            ss = s[i:]
            for key in dt.keys():
                if ss.startswith(key):
                    # print(ss, key, i, len(key))
                    answer += dt[key]
                    i += len(key)
                    break       # !
        
        return answer
                    
        