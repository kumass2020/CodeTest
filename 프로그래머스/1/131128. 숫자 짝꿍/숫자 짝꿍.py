from collections import Counter

def solution(X, Y):
    answer = ''
#     paired_num_list = []
    
#     for num_x in X:
#         # count = 0
#         for num_y in Y.split(' '):
#             if num_x == num_y:
#                 paired_num_list.append(num_y)
#                 Y.pop(num_y)
#                 # count += 1
#                 break
    
#     if paired_num_list:
#         answer = ''.join(sorted(paired_num_list))
#     else: 
#         answer = '-1'

    count_x = Counter(X)
    count_y = Counter(Y)
    
    common_digits = []
    for digit in count_x.keys():
        if digit in count_y:
            common_digits.extend([digit] * min(count_x[digit], count_y[digit]))
    
    if not common_digits:
        return "-1"
            
    result = ''.join(sorted(common_digits, reverse=True))
    
    if result[0] == '0':
        return "0"
                
    return result