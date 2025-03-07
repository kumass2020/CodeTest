def solution(places):
    answer = []
    
    seat_to_check = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) <= 2 and (i != 0 or j != 0):
                seat_to_check.append((i, j))
    
    
    for place in places:
        counter = 0
        for i, row in enumerate(place):
            for j, elem in enumerate(row):
                if counter == 0:
                    if place[i][j] == "P":
                        for move in seat_to_check:
                            x = i + move[0]
                            y = j + move[1]

                            if (0 <= x <= 4) and (0 <= y <= 4) and place[x][y] == "P":
                                if abs(i-x) == 2:
                                    if place[i + move[0]//2][y] == "X":
                                        pass
                                    else:
                                        answer.append(0)
                                        counter += 1
                                        break
                                elif abs(j-y) == 2:
                                    if place[x][j + move[1]//2] == "X":
                                        pass
                                    else:
                                        answer.append(0)
                                        counter += 1
                                        break
                                elif abs(i-x) == 1 and abs(j-y) == 1:
                                    if place[i][y] == "X" and place[x][j] == "X":
                                        pass
                                    else:
                                        answer.append(0)
                                        counter += 1
                                        break
                                else:       
                                    answer.append(0)
                                    counter += 1
                                    break
                                
                else:
                    break
                
        if not counter:
            answer.append(1)
                                
                
                            
                    
    
    return answer