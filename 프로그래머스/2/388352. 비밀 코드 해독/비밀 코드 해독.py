def solution(n, q, ans):
    answer = 0
    M = len(q)
    
    def ans_count(candidates, cur_q, cur_ans):
        ans_count = 0
        for num in candidates:
            if num in cur_q:
                ans_count += 1
        if ans_count == cur_ans:
            return True
        else:
            return False
        

    # def dfs(idx, candidates):
#         nonlocal answer
        
#         cur_q = q[idx_q]
#         cur_ans = ans[idx_q]
        
#         if idx_q == M:
#             if ans_count(candidates, cur_q, cur_ans):
#                 answer += 1
#             # else:
#                 # continue
        
#         new_candidates = candidates[:]
#         count = 0
#         for i in range(5):
#             if len(new_candidates) <= 4 and count <= cur_ans:
#                 new_candidates.append(cur_q[i])
#                 count += 1
#                 new_candidates = sorted(new_candidates) if len(new_candidates) > 0 else new_candidates
#                 print(new_candidates)
#                 if len(new_candidates) >= cur_ans and ans_count(new_candidates, cur_q, cur_ans):
#                     dfs(idx_q+1, new_candidates)
#             elif len(new_candidates) > 5 or count > cur_ans:
#                 new_candidates.pop()
#                 count -= 1

    def dfs(idx, candidates):
        nonlocal answer 
        M = len(q)
        
        if len(candidates) == 5:
            for i in range(M):
                cur_q = q[i]
                cur_ans = ans[i]
                
                if not ans_count(candidates, cur_q, cur_ans):
                    break
                    
                if i == M-1:
                    answer += 1
        
        new_candidates = candidates[:]
        for i in range(idx, n+1):
            if len(candidates) < 5:
                new_candidates.append(i)
                # print(new_candidates)
                dfs(i+1, new_candidates)
                new_candidates.pop()
                
    
    dfs(1, [])
    return answer