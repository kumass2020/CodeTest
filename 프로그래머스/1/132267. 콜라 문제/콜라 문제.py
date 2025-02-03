def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += b * int(n / a)
        n = b * (int(n / a)) + (n % a)
    
    return answer