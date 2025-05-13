def solution(numbers, target):
    answer = 0
    
    N = len(numbers)
    def dfs(idx, lst):
        nonlocal answer
        # print(lst)
        
        if len(lst) == N and sum(lst) == target:
            answer += 1
            return
            
        new_lst = lst[:]
        # for i in range(idx, N):
        if idx <= N-1:
            for coeff in [-1, 1]:
                new_lst.append(coeff*numbers[idx])
                dfs(idx+1, new_lst)
                new_lst.pop()
    
    dfs(0, [])
    
    return answer