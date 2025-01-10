# def solution(n, m, section):
#     answer = 0
    
#     dist = section[-1] - section[0]
#     tries = int(dist / m) + 1
    
#     if tries > len(section):
#         tries = len(section)
    
#     for i in section:
#         section_2 = section.copy()
#         section_2.remove(i)
#         for j in section_2:
#             if abs(j - i) < m:
#                 tries -= 0.5
    
#     answer = tries
    
#     return answer

def solution(n, m, section):
    count = 0       # 최소 페인트칠 횟수
    end = 0         # 현재까지 칠해진 마지막 구역 번호
    
    for sec in section:
        # 아직 칠하지 않은 구역이 나오면 새로 롤러질해야 함
        if sec > end:
            count += 1
            end = sec + (m - 1)  # 이번 롤러질로 칠해지는 마지막 구역 번호
    
    return count
