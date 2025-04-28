def solution(sequence):
#     # answer = 0
    
#     # pulse = 1
#     summ = 0
#     max_summ = float('-inf')
#     i = j = 0
#     while i < len(sequence):
#         while j < len(sequence):
#             num = sequence[j] * ((-1)**(j % 2))
#             # print(i, j, num, summ, max_summ)
#             if summ * num < 0:
#                 break
#             else:
#                 summ += num
#                 max_summ = max(max_summ, abs(summ))
#                 j += 1
        
        
#         i = j
#         summ = 0

    # max_summ == float('-inf')
    A1 = [0] * len(sequence)
    A2 = [0] * len(sequence)
    A1[0] = sequence[0] * (-1)
    A2[0] = sequence[0]
    for i in range(1, len(sequence)):
        pulse1 = -1 if i % 2 == 0 else 1
        pulse2 = -1 * pulse1
        
        # num1 = sequence[i]
        # num2 = sequence[i-1]
        
        A1[i] = max(sequence[i] * pulse1, A1[i-1] + sequence[i] * pulse1)
        A2[i] = max(sequence[i] * pulse2, A2[i-1] + sequence[i] * pulse2)
    
    return max(max(A1), max(A2))