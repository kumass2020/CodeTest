def solution(s):
    answer = []
    
    for i, character in enumerate(s):
        result = -1
        if i == 0: 
            pass
        else: 
            for j in range(i-1, -1, -1):
                if result == -1:
                    if s[j] == s[i]:
                        result = i-j
                    
                
        answer.append(result)
    
    return answer