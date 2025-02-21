# def solution(picks, minerals):
#     answer = 0
    
#     minerals_per_pick = []
    
#     for i in range(0, len(minerals)-1, 5):
#         if i+4 <= len(minerals)-1:
#             minerals_per_pick.append(minerals[i:i+5])
#         else: 
#             minerals_per_pick.append(minerals[i:])
        
#     dia_fatigue = []
#     iron_fatigue = []
#     stone_fatigue = []
#     for mineral_set in minerals_per_pick:
#         dia_f = 0
#         iron_f = 0
#         stone_f = 0
#         for mineral in mineral_set:
#             if mineral == 'diamond':
#                 dia_f += 1
#                 iron_f += 5
#                 stone_f += 25
#             elif mineral == 'iron':
#                 dia_f += 1
#                 iron_f += 1
#                 stone_f += 5
#             elif mineral == 'stone':
#                 dia_f += 1
#                 iron_f += 1
#                 stone_f += 1
        
#         dia_fatigue.append(dia_f)
#         iron_fatigue.append(iron_f)
#         stone_fatigue.append(stone_f)
    
#     # 다이아 곡괭이 만큼 반복
#     for i in range(picks[0]):
#         max_dia = max(dia_fatigue)
#         max_dia_idx = dia_fatigue.index(max_dia)
        
#         answer += max_dia
#         dia_fatigue.pop(max_dia_idx)
#         iron_fatigue.pop(max_dia_idx)
#         stone_fatigue.pop(max_dia_idx)
        
#         if not len(dia_fatigue):
#             return answer
    
#     for i in range(picks[1]):
#         max_iron = max(iron_fatigue)
#         max_iron_idx = iron_fatigue.index(max_iron)
        
#         answer += max_iron
#         iron_fatigue.pop(max_iron_idx)
#         stone_fatigue.pop(max_iron_idx)
        
#         if not len(iron_fatigue):
#             return answer
        
#     for i in range(picks[2]):
#         max_stone = max(stone_fatigue)
#         max_stone_idx = stone_fatigue.index(max_stone)
        
#         answer += max_stone
#         stone_fatigue.pop(max_stone_idx)
        
#         if not len(stone_fatigue):
#             return answer
    
#     return answer

# # 중간에 처리가 안된 광물이 있다면 ??

def solution(picks, minerals):
    total_picks = sum(picks)
    
    max_minerals = total_picks * 5
    minerals = minerals[:max_minerals]
    
    groups = []
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        
        stone_cost = 0
        for m in group:
            if m == "diamond":
                stone_cost += 25
            elif m == "iron":
                stone_cost += 5
            else:
                stone_cost += 1
        groups.append((stone_cost, group))
    
    groups.sort(key=lambda x: x[0], reverse=True)
    
    answer = 0
    
    for _, group in groups:
        if picks[0] > 0:
            picks[0] -= 1
            answer += len(group) * 1
        elif picks[1] > 0:
            picks[1] -= 1
            for m in group:
                if m == "diamond":
                    answer += 5
                else:
                    answer += 1
        elif picks[2] > 0:
            picks[2] -= 1
            for m in group:
                if m == "diamond":
                    answer += 25
                elif m == "iron":
                    answer += 5
                else:
                    answer += 1
    
    return answer