# def solution(n, k):
#     answer = 0
    
#     numbers = []
#     res = n
#     for i in range(15, -1, -1):
#         if res == 0:
#             numbers.append(0)
#             continue
        
#         # n = res
        
#         num = res // (k ** i)
#         res = res - (num * k ** i)
        
#         numbers.append(num)
        
#     new_numbers = numbers
#     for i in range(15):
#         if new_numbers[0] == 0:
#             new_numbers.pop(0)
#     numbers = new_numbers
    
#     def is_prime(number_str):
#         if number_str:
#             prime_count = 0
#             x = int(number_str)
#             if x != 1:
#                 for i in range(1, x+1):
#                     if x % i == 0:
#                         prime_count += 1
#                     if prime_count >= 2 and i != x:
#                         return False
#                 if prime_count <= 2:
#                     return True
#             else:
#                 return False    
    
#     number_str = ''
#     for i, num in enumerate(numbers):
#         if num != 0:
#             number_str += str(num)
#             if len(number_str) == len(numbers):
#                 if is_prime(number_str):
#                     return 1
#             if i == len(numbers)-1:
#                 if is_prime(number_str):
#                     answer += 1
                
#         else:
#             if is_prime(number_str):
#                 answer += 1
#             number_str = ''
            
#     return answer

import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def convert_to_base(n, k):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n % k) + s
        n //= k
    return s

def solution(n, k):
    answer = 0
    
    base_k_str = convert_to_base(n, k)
    
    candidates = base_k_str.split("0")
    
    for cand in candidates:
        if cand == "":
            continue
        x = int(cand)
        if is_prime(x):
            answer += 1
    
    return answer
