def solution(name, yearning, photo):
    answer = []
#     omoide_dict = {}
    
#     for _name in name:
#         omoide_dict[_name] = 
        
    omoide_dict = {_name: yearning[i] for i, _name in enumerate(name)}
    
    for _photo in photo:
        score = 0
        for __name in _photo:
            if __name in name:
                score += omoide_dict[__name]
        
        answer.append(score)
    
    return answer