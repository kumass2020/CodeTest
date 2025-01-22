def solution(food):
    answer = ''
    
    for i, num in enumerate(reversed(food)):
        # if i == 0:
        #     answer += str(i)
        if i == 0:
            answer = '0'
        if num == 0:
            pass
        else:
            answer = int(num / 2) * str(len(food)-1-i) + answer + int(num / 2) * str(len(food)-1-i)
        
        
    
    return answer