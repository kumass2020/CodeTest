# def solution(scores):
#     answer = 0
    
#     min_attitude = 100001
#     min_peer = 100001
#     max_attitude = -1
#     max_peer = -1
    
#     wanho = scores[0]
    
#     for score in scores:
#         attitude = score[0]
#         peer = score[1]
        
#         if attitude < min_attitude:
#             min_attitude = attitude
#         if peer < min_peer:
#             min_peer = peer
            
#         if attitude > max_attitude:
#             max_attitude = attitude
#         if peer > max_peer:
#             max_peer = peer
            
#         if wanho[0] < attitude and wanho[1] < peer:
#             return -1
#     # print(min_attitude, min_peer)
#     new_scores = []
#     for i, score in enumerate(scores):
#         attitude = score[0]
#         peer = score[1]
        
#         if min_attitude <= attitude <= max_attitude or min_peer <= peer <= max_peer:
#             new_scores.append([attitude, peer, attitude+peer])
    
#     print(new_scores)
#     scores = new_scores
#     scores.sort(key=lambda x: x[2], reverse=True)
    
#     # print(scores)
#     rank = 0
#     buffer = 0
#     prev_score = 200001
#     for score in scores:
#         cur_score = score[2]
#         if cur_score < prev_score:
#             prev_score = cur_score
#             if buffer:
#                 rank += buffer 
#                 buffer = 0
#             rank += 1
#         elif cur_score == prev_score:
#             buffer += 1
        
#         if score == wanho:
#             return rank
#             # if not buffer:
#             #     return rank
#             # if buffer:
#             #     return rank+1
    
        
    
#     # return answer


def solution(scores):
    answer = 0
    target_a, target_b = scores[0]  # 완호 점수
    target_score = target_a + target_b  # 완호 점수 합

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬합니다.
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0
    
    for a, b in scores: # score 순회
        if target_a < a and target_b < b:   # 완호보다 둘 다 높으면 -1
            return -1
        
        if b >= maxb:   # 앞의 점수가 a가 같거나 낮고, b가 같거나 높음
            maxb = b    # 최대 b 기록
            if a + b > target_score:    # 합산 점수가 완호보다 높으면
                answer += 1             # 순위 하나 밀림
        
    return answer + 1