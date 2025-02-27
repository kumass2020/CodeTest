# def solution(users, emoticons):
#     answer = []
    
#     # for i in range(len(emoticons)):
#     #     for j in range(len(emoticons)):
#     #         total_price = 0
#     #         for k in [10, 20, 30, 40]:
#     #             total_price += k *
    
#     for i in range(len(emoticons)):
#         for j in range(len(emoticons)):
#             total_price += emoticons[i]
#             if i != j:
                
        
    
#     return answer

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    m = len(emoticons)
    n = len(users)
    
    best = (0, 0)
    
    def dfs(idx, current_discounts):
        nonlocal best
        
        if idx == m:
            subscribers = 0
            revenue = 0
            for disc_threshold, price_threshold in users:
                total = 0 
                for j in range(m):
                    d = current_discounts[j]
                    
                    if d >= disc_threshold:
                        total += emoticons[j] * (100 - d) // 100
                if total >= price_threshold:
                    subscribers += 1
                else:
                    revenue += total
            
            if subscribers > best[0] or (subscribers == best[0] and revenue > best[1]):
                best = (subscribers, revenue)
            return
        
        for rate in discount_rates:
            current_discounts.append(rate)
            dfs(idx + 1, current_discounts)
            current_discounts.pop()
    
    dfs(0, [])
    return [best[0], best[1]]