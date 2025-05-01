def solution(answers):
    # answer = []
    
    p1 = (1,2,3,4,5)
    p2 = (2,1,2,3,2,4,2,5)
    p3 = (3,3,1,1,2,2,4,4,5,5)
    
    c1 = c2 = c3 = 0
    for i, a in enumerate(answers):
        if p1[i%5] == a:
            c1 += 1
        if p2[i%8] == a:
            c2 += 1
        if p3[i%10] == a:
            c3 += 1
            
    if c1 == c2 == c3:
        return [1,2,3]
    elif c1 == c2 > c3:
        return [1,2]
    elif c2 == c3 > c1:
        return [2,3]
    elif c3 == c1 > c2:
        return [1,3]
    elif max(c1,c2,c3) == c1:
        return [1]
    elif max(c1,c2,c3) == c2:
        return [2]
    else: return [3]
    
    # return answer