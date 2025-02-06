def solution(sequence, k):
    candidates = []
    # for i, number in enumerate(sequence):
        # start = i
        
        # for end in range(start, len(sequence)):
        #     partial_sum = sum(sequence[start:end+1])
        #     if partial_sum == k:
        #         candidates.append((start, end))
        #         break
        
    # end = len(sequence)
    
#     for i in range(len(sequence)-1, -1, -1):
#         end = i
#         for start in range(end, -1, -1):
#             partial_sum = sum(sequence[start:end+1])
#             if partial_sum == k:
#                 candidates.append((start, end))
#                 break
        
#     if len(candidates) == 1:
#         return candidates[-1]
    
#     candidates_lengths = []
#     for candidate in candidates:
#         candidates_lengths.append(candidate[1] - candidate[0])
    
#     if max(candidates_lengths) == min(candidates_lengths):
#         return candidates[-1]
#     else:
#         return candidates[0]

    n = len(sequence)
    left = 0
    current_sum = 0
    best_length = float('inf')
    answer = [0, 0]
    
    # 오른쪽으로 윈도우 확장
    for right in range(n):
        # 확장된 만큼 current_sum에 누적
        current_sum += sequence[right]
        
        # 확장되어서 current_sum이 k이상이거나, right이 left 이상일 때, 
        while current_sum >= k and left <= right:
            # 합이 k를 만족할 경우
            if current_sum == k:
                # 부분 수열의 길이
                length = right - left + 1
                # 길이 짧은 경우에만 저장
                if length < best_length:
                    best_length = length
                    answer = [left, right]
            
            # 이제 오른쪽으로 확장하면 무조건 k보다 커지므로, 윈도우의 왼쪽을 당겨옴
            current_sum -= sequence[left]
            left += 1
    
    return answer