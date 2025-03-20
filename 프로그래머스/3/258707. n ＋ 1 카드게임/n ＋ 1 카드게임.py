# def solution(coin, cards):
#     answer = 0
    
#     n = len(cards)
#     k = n // 6
    
#     Rounds = [[] for i in range(4*k)]
    
#     my_cards = cards[:2*k]
#     left = cards[2*k:]
    
    
    
#     cards_target = [0] * n
#     for i, num in enumerate(cards):   # find estimated round
#         target = n+1 - num
#         target_pos = max(i, cards.find(target))
#         cards_target[i] = target_pos
    
#     for i in range(2*k):    # i: current round
#         counter = 0
#         cur_cards = [left[2i], left[2i+1]]
        
#         if cur_card in cur_cards:
#             if coin and cards_target[]
        
#         for m in range(len(my_cards)):
#             for n in range(m+1, len(my_cards))
#                 if my_cards[m] + my_cards[n] == n+1:
#                     counter += 1
#                     _my_cards = my_cards[:]
#                     _my_cards.remove(m)
#                     _my_cards.remove(n)
#                     my_cards = _my_cards
#                     break
#             if counter:
#                 break
        
#         if not counter:
#             return i+1
        
#     return answer


def solution(coin, cards):
    n = len(cards)
    Round = n // 3
    
        
    my_cards = cards[:Round]
    left = cards[Round:]
    round_cards = []
    
    for i in range(Round):
        counter = 0
        round_cards.extend([left[2*i], left[2*i+1]])
        
        for m in range(len(my_cards)):
            for l in range(m+1, len(my_cards)):
                if my_cards[m] + my_cards[l] == n+1:
                    counter += 1
                    _my_cards = my_cards[:]
                    _my_cards.pop(l)
                    _my_cards.pop(m)
                    my_cards = _my_cards
                    break
            if counter:
                break
        if counter:
            continue
        
        # 기존 카드에서 해결이 안되면..
        if coin >= 1:
            for m in range(len(my_cards)):
                for l in range(len(round_cards)):
                    if my_cards[m] + round_cards[l] == n+1:
                        counter += 1
                        _my_cards = my_cards[:]
                        _round_cards = round_cards[:]
                        _my_cards.pop(m)
                        _round_cards.pop(l)
                        my_cards = _my_cards
                        round_cards = _round_cards
                        coin -= 1
                        break
                if counter:
                    break
            if counter:
                continue
        else:
            return i+1
                
        
        if coin >= 2:
            for m in range(len(round_cards)):
                for l in range(m+1, len(round_cards)):
                    if round_cards[m] + round_cards[l] == n+1:
                        counter += 1
                        _round_cards = round_cards[:]
                        _round_cards.pop(l)
                        _round_cards.pop(m)
                        round_cards = _round_cards
                        coin -= 2
                        break
                if counter:
                    break
            if counter:
                continue
        else:
            return i+1

        if counter == 0:
            return i+1
    

    return Round+1