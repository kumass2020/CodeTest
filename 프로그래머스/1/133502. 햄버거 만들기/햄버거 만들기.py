def solution(ingredient):
    answer = 0
    
#     bun = ingredient.count(1) / 2
#     vegi = ingredient.count(2)
#     meat = ingredient.count(3)
    
#     answer = min([bun, vegi, meat])
    stack = []

    for item in ingredient:
#         if elem == 1:
#             if bun >= 1 and vegi >= 1 and meat >= 1:
#                 bun_upper += 1 
#             else:
#                 bun += 1
#         elif elem == 2:
#             if bun > vegi:
#                 vegi += 1
#         elif elem == 3:
#             if bun > meat and vegi > meat:
#                 meat += 1
        
#         if bun_upper:
#             answer += 1
#             bun -= 1
#             vegi -= 1
#             meat -= 1
#             bun_upper -= 1

        stack.append(item)
    
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
            
            
    
    return answer