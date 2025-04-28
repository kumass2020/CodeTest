def solution(m, n, startX, startY, balls):
    answer = []
    
    dots = [(-startX, startY), (startX, -startY), (startX, 2*n-startY), (2*m-startX, startY)]
    
    
    for ball in balls:
        min_dist = float('inf')
        for dot in dots:
            # print((startX, startY), dot, ball, min_dist)
            # if ball in [[0,0], [m, 0], [0, n], [m, n]]:
                
            
            if dot[1] == ball[1]:
                if (startX < ball[0] < dot[0]) or (dot[0] < ball[0] < startX):
                    continue
            elif dot[0] == ball[0]:
                if (startY < ball[1] < dot[1]) or (dot[1] < ball[1] < startY):
                    continue
            
            dist1 = (dot[0]-ball[0])**2
            dist2 = (dot[1]-ball[1])**2
            
            min_dist = min(min_dist, dist1+dist2)
            
        answer.append(min_dist)
    
    return answer