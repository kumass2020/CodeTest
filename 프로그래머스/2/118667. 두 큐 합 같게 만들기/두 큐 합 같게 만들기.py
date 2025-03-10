from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    len_q1 = len(q1)
    len_q2 = len(q2)
    
    while sum_q1 != sum_q2:
        if sum_q1 < sum_q2:
            num = q2.popleft()
            q1.append(num)
            sum_q1 += num
            sum_q2 -= num
        else:
            num = q1.popleft()
            q2.append(num)
            sum_q1 -= num
            sum_q2 += num
            
        answer += 1
        
        if answer > (len_q1 + len_q2) * 2:
            return -1
        
    return answer