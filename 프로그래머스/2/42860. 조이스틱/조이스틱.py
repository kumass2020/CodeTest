def solution(name):
    answer = 0
    
#     forward = 0
#     count = 0
#     for c in name:
#         count += 1
#         if c != 'A':
#             forward += count
#     backward = 0
#     count = 0
#     for c in name[::-1]:
#         count += 1
#         if c != 'A':
#             backward += count
    
#     print(forward, backward)
#     answer += min(forward, backward)

    # dp = [0] * len(name)
    # dp[0] = 0
    # dp[-1] = 1
    # dp[1] = 1
    # for i in range(2, len(name)-1):
    #     dp[i] = dp[i-1] + dp[i+1]
    n = len(name)
    x = n-1
    for i in range(n):
        j = i+1
        while j < n and name[j] == 'A':
            j += 1
        x = min(x, 2*i + (n-j), 2*(n-j) + i)
    answer += x
    
    for i, c in enumerate(name):
        # if i >= 1:
        #     if c != 'A':
        #         answer += 1
            
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
        
    
    # print(ord('A'))
    # print(chr(65))
    # print(ord('Z'))
    
    return answer