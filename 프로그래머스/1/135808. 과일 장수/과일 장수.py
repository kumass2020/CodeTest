def solution(k, m, score):
    answer = 0
    
    sorted_score = sorted(score, reverse=True)
    for i in range(int(len(score) / m)):
        answer += m * sorted_score[(i+1)*m-1]
    
    
    return answer