def solution(bandage, health, attacks):
    answer = 0
    
    # timestamp = 0
    attack_idx = 0
    cont_count = 0
    max_health = health
    
    for timestamp in range(attacks[-1][0]+1):
        if timestamp > 0:
            if attacks[attack_idx][0] == timestamp:
                health -= attacks[attack_idx][1]
                cont_count = 0

                if health <= 0:
                    answer = -1
                    break

                attack_idx += 1
            else:
                # if timestamp > 0:
                cont_count += 1
                health += bandage[1]
                if cont_count > 0 and cont_count % bandage[0] == 0:
                    health += bandage[2]
                    cont_count = 0
                if health > max_health:
                    health = max_health

            answer = health
    
    return answer