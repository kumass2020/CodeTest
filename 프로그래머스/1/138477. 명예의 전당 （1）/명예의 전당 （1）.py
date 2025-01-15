def solution(k, score):
    answer = []
    score_list = []
    
    for i, _score in enumerate(score):
        score_list.append(_score)
        score_list = sorted(score_list, reverse=True)
        if i >= k-1:    
            answer.append(score_list[k-1])
        else:
            answer.append(score_list[-1])
    
    return answer