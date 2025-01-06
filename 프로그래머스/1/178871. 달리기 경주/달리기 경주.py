# def solution(players, callings):
#     answer = []
#     values = [i for i in range(len(players))]
#     for call in callings:
#         idx = players.index(call) 
#         values[idx] -= 1
        
#         # idx = players.index(call)
#         # temp = players[idx-1]
#         # players[idx-1] = players[idx]
#         # players[idx] = temp
        
#         # following_name = players[idx]
#         # preceding_name = players[idx-1]
#         # players[idx-1] = following_name
#         # players[idx] = preceding_name
    
#     sorted_pairs = sorted(zip(values, players))
#     sorted_values, sorted_names = zip(*sorted_pairs)
    
#     answer = sorted_names
    
def solution(players, callings):
    # Create a dictionary to map player names to their indices
    positions = {player: i for i, player in enumerate(players)}
    
    # Process each call
    for call in callings:
        current_idx = positions[call]
        
        # Swap the called player with the player in front
        if current_idx > 0:  # Ensure they aren't already in first place
            preceding_player = players[current_idx - 1]
            
            # Swap in the players list
            players[current_idx], players[current_idx - 1] = (
                players[current_idx - 1],
                players[current_idx],
            )
            
            # Update the positions dictionary
            positions[call] -= 1
            positions[preceding_player] += 1
    
    return players

    return answer