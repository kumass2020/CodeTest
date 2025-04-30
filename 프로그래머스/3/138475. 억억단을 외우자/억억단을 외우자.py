# def solution(e, starts):
#     answer = []
    
#     dp = [0] * (e+1)
    
#     # 각 수의 약수의 개수 계산
#     for i in range(1, e+1):
#         count = 0
#         for j in range(1, int(i**0.5+1)):
#             if i % j == 0:
#                 count += 1
#                 if j == i**0.5:
#                     count -= 0.5
#         count *= 2
#         dp[i] = count
        
#     # start마다 약수 많은 것 선택
    
#     idx = -1
#     for start in starts:
#         # if start < idx:
#         #     answer.append(idx)
#         #     continue
#         # else:
#         #     idx = -1
#         idx = -1
#         maxx = 0
#         for i in range(start, e+1):
#             if maxx < dp[i]:
#                 idx = i
#                 maxx = dp[i]
#                 continue
#         answer.append(idx)
    
#     return answer

def build_divisor_counts(e):
    spf = [0] * (e + 1)     # spf[x] = x의 최소 소인수
    dp = [0] * (e + 1)      # dp[x]  = x의 약수 개수
    primes = []

    # 1은 특별취급
    dp[1] = 1
    spf[1] = 1

    # 선형 체로 최소 소인수 채우기
    for i in range(2, e + 1):
        if spf[i] == 0:     # 최소 소인수 없는 경우는 최대인 i로 채워줌
            spf[i] = i
            primes.append(i) # 이 경우 i는 소수임
        for p in primes:
            if p > spf[i] or i * p > e: # 다 봤으면 for문 탈출
                break
            spf[i * p] = p  # 최소 소인수

    # 약수 개수 계산: 소인수 분해 기반 공식 사용
    # dp 계산: i = m * p^k 꼴로 분해
    for i in range(2, e + 1):
        p = spf[i]
        m = i // p
        k = 1
        while m % p == 0:
            m //= p 
            k += 1  # 지수
        
        # 약수의 분할 정리: τ(i) = τ(m) * (k+1)
        dp[i] = dp[m] * (k + 1) # 지수 + 1을 곱하기

    return dp

def build_suffix_best(dp):
    e = len(dp) - 1
    best = [0] * (e + 2)
    best[e] = e

    # 뒤에서부터 보며 가장 약수 많은 수 저장
    for i in range(e - 1, 0, -1):
        # 같으면 더 작은 수 선택
        if dp[i] >= dp[best[i + 1]]:
            best[i] = i
        else:
            best[i] = best[i + 1]

    return best

def solution(e, starts):
    dp = build_divisor_counts(e)
    best = build_suffix_best(dp)
    return [best[s] for s in starts]