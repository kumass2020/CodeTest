def solution(numbers):
    answer = [-1] * len(numbers)
    
    # (idx, val)
    stack = []
    for i in range(len(numbers)):

        while stack:
            if stack[-1][1] < numbers[i]:
                idx, _ = stack.pop()
                answer[idx] = numbers[i]
            else:
                break
        
        stack.append((i, numbers[i]))
        
        
    
    return answer