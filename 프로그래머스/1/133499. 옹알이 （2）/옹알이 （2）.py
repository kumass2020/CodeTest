def solution(babbling):
    answer = 0
    
    for item in babbling:
        queue = []
        prev_word = ''
        target = item
        for i, character in enumerate(target):
            queue.append(character)
            queue_str = ''.join(queue)
            if len(queue) >= 3: 
                if (queue_str[:3] == "aya" or queue_str[:3] == "woo"):
                    if queue_str[:3] == prev_word:
                        break
                    else:
                        prev_word = queue_str[:3]
                        for _ in range(3):
                            queue.pop(0)
                else:
                    break
            if len(queue) >= 2: 
                if (queue_str[:2] == "ye" or queue_str[:2] == "ma"):
                    if queue_str[:2] == prev_word:
                        break
                    else:
                        prev_word = queue_str[:2]
                        for _ in range(2):
                            queue.pop(0) 
            
            if i == len(target)-1 and len(queue) == 0:
                answer += 1
    
    return answer