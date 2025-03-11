def solution(players, m, k):
    answer = 0
    
    server_expansion = []
    
    for i, player in enumerate(players):
        handled_player = 0
        if i >= 1:
            for j in range(i-1, max(-1, i-k), -1):
                handled_player += server_expansion[j] * m

        player -= handled_player
        player = player if player >= 0 else 0
        server_expansion.append(player // m)
            
        
    answer = sum(server_expansion)
    return answer