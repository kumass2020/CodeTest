def solution(friends, gifts):
    answer = 0
    relations = {friend: {_friend: 0 for _friend in friends} for friend in friends}
    gift_points = {friend: 0 for friend in friends}
    
    for gift in gifts:
        gift_list = gift.split(" ")
        sender = gift_list[0]
        receiver = gift_list[1]
        
        # 주고받은 선물
        relations[sender][receiver] += 1
        
        # 선물 지수
        gift_points[sender] += 1
        gift_points[receiver] -= 1
            
    next_month_receive = {friend: 0 for friend in friends}
    
    for i, friend in enumerate(friends):
        for j in range(i+1, len(friends)):
            if relations[friends[i]][friends[j]] > relations[friends[j]][friends[i]]:
                next_month_receive[friends[i]] += 1
            elif relations[friends[i]][friends[j]] == relations[friends[j]][friends[i]]:
                if gift_points[friends[i]] > gift_points[friends[j]]:
                    next_month_receive[friends[i]] += 1
                elif gift_points[friends[i]] == gift_points[friends[j]]:
                    pass
                elif gift_points[friends[i]] < gift_points[friends[j]]:
                    next_month_receive[friends[j]] += 1
            elif relations[friends[i]][friends[j]] < relations[friends[j]][friends[i]]:
                    next_month_receive[friends[j]] += 1
        
    answer = max(next_month_receive.values())
    
    return answer