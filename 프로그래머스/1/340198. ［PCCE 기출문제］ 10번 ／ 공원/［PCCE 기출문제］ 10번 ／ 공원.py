def solution(mats, park):
    answer = 0
    accepted_mat = -1

    for mat in sorted(mats, reverse=True):
        if mat > min(len(park[0]), len(park[1])):
            continue
        if accepted_mat != -1:
            continue
        
        for i in range(len(park[0])):
            for j in range(len(park[1])):
                accepted = True
                if i + mat > len(park) or j + mat > len(park[1]):
                    continue
                
                for k in range(mat):
                    for l in range(mat):
                        if park[i+k][j+l] != "-1":
                            accepted = False
                
                if not accepted:
                    continue
                
                if accepted:
                    # idx = (i, j)
                    accepted_mat = mat
                
        # if accepted:
        #     continue
    
    if accepted:
        answer = accepted_mat
    else:
        answer = -1
        
    
    return answer