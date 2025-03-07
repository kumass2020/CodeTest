# def solution(orders, course):
#     answer = []
    
#     orders_dict = {}
    
#     # 각 order에서 가능한 모든 조합을 DFS로 찾고 count ++ 
#     def dfs(index, path, order):
#         if len(path) >= 1:
#             path_str = ''.join(path)
#             if orders_dict.get(path_str):
#                 orders_dict[path_str] += 1
#             else:
#                 orders_dict[path_str] = 1
        
#         for i in range(index, len(order)):
#             path.append(order[i])
#             dfs(i+1, path, order)
#             path.pop()
    
#     for order in orders:
#         dfs(0, [], order)
    
#     # count가 2 이상이고 course를 만족하는 dictionary의 key를 result에 추가
#     matched_course = [key for key, value in orders_dict.items() 
#                   if len(key) in course and value >= 2]
    
#     # result는 알파벳 오름차순 정렬
#     matched_course.sort()
    
#     return matched_course

def solution(orders, course):
    orders_dict = {}
    
    # DFS를 이용해 각 주문에서 가능한 모든 조합(길이가 2 이상)을 생성하고 count를 증가합니다.
    def dfs(index, path, order):
        if len(path) >= 2:  # 코스 요리는 최소 2개의 메뉴여야 합니다.
            path_str = ''.join(path)
            orders_dict[path_str] = orders_dict.get(path_str, 0) + 1
        for i in range(index, len(order)):
            path.append(order[i])
            dfs(i + 1, path, order)
            path.pop()
    
    # 각 주문을 알파벳 순으로 정렬한 후 DFS로 조합을 생성합니다.
    for order in orders:
        sorted_order = sorted(order)
        dfs(0, [], sorted_order)
    
    result = []
    # course에 주어진 각 길이별로 주문 횟수가 2회 이상인 조합 중 최빈 조합만 선택합니다.
    for c in course:
        # 길이가 c이고 주문 횟수가 2 이상인 후보들을 모읍니다.
        valid = [(menu, count) for menu, count in orders_dict.items() if len(menu) == c and count >= 2]
        if not valid:
            continue
        max_count = max(count for menu, count in valid)
        # 최대 주문 횟수를 가진 조합만 결과에 추가합니다.
        result.extend([menu for menu, count in valid if count == max_count])
    
    return sorted(result)