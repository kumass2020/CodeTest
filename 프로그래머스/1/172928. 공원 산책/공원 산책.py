def solution(park, routes):
    answer = []
    # pos = [0, 0]
    for i, row in enumerate(park):
        if 'S' in park[i]:
            idx_0 = i
            idx_1 = park[i].find('S')
            pos = [idx_0, idx_1]
            
    for route in routes:
        pos_prev = pos.copy()
        is_collide = 0
        
        for i in range(int(route[-1])):
            if route[0] == 'E':
                if pos[1]+1 <= len(park[0])-1:
                    if park[pos[0]][pos[1]+1] != 'X':
                        pos[1] += 1
                    else: is_collide += 1
                else: is_collide += 1
                
            if route[0] == 'S':
                if pos[0]+1 <= len(park)-1:
                    if park[pos[0]+1][pos[1]] != 'X':
                        pos[0] += 1
                    else: is_collide += 1
                else: is_collide += 1
                
            if route[0] == 'W':
                if pos[1]-1 >= 0:
                    if park[pos[0]][pos[1]-1] != 'X':
                        pos[1] -= 1
                    else: is_collide += 1
                else: is_collide += 1
                
            if route[0] == 'N':
                if pos[0]-1 >= 0:
                    if park[pos[0]-1][pos[1]] != 'X':
                        pos[0] -= 1
                    else: is_collide += 1
                else: is_collide += 1
                
        if is_collide > 0:
            pos = pos_prev
        
    answer = pos
    
    return answer