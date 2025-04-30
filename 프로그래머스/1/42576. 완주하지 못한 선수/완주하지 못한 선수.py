def solution(participant, completion):
    # answer = ''
    # print(set(participant) & set(completion))
    
#     for p in participant:
#         if p not in comp:
#             return p

    dt = {}
    for c in completion:
        dt[c] = dt.get(c, 0) + 1
        
    for p in participant:
        dt[p] = dt.get(p, 0) - 1
        if dt[p] < 0:
            return p
        
    # for key, value in dt.items():
    #     for i in range(value):
    #         dt.key[]
    
    # return answer