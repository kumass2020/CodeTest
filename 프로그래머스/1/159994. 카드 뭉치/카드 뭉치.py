def solution(cards1, cards2, goal):
    answer = ''
    result = "Yes"
    
    for word in goal:
        is_goal = False
        if result == "Yes":
            if len(cards1) > 0:
                if word == cards1[0]:
                    cards1.pop(0)
                    is_goal = True
            if len(cards2) > 0:
                if word == cards2[0]:
                    cards2.pop(0)
                    is_goal = True
            if not is_goal:
                result = "No"
    answer = result
    return answer