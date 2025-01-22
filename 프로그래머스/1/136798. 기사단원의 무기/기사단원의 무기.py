def solution(number, limit, power):
#     answer = 0
#     divisors_dict = {}
    
#     # if divisors_dict[number-1]:
#     #     pass
    
#     for _number in range(number, 0, -1):
#         if not _number in divisors_dict.keys():
#             divisors_dict[_number] = 0
            
#             for num in range(1, _number+1):
#                 if _number % num == 0:
#                     divisors_dict[_number] += 1
#         else:
#             pass
        
    
#     for num in range(1, number+1):
#         count = divisors_dict[num]
        
#         answer += count if count <= limit else power
            
    
#     return answer

    # Precompute divisor counts
    divisors_count = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors_count[j] += 1

    # Calculate the required iron weight
    answer = 0
    for count in divisors_count[1:]:
        if count > limit:
            answer += power
        else:
            answer += count
    
    return answer