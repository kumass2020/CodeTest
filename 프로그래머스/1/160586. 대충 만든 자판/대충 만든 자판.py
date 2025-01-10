def solution(keymap, targets):
    answer = []

    for target in targets:
        count = 0
        result = 0
        for character in target:
            if character not in ''.join(keymap):
                result = -1
                continue
            else:
                min_key_idx = 100
                for keys in keymap:
                    for i, key in enumerate(keys):
                        if key == character and i < min_key_idx:
                            min_key_idx = i
                count += min_key_idx + 1
                  
        if result == -1:
            answer.append(result)
            continue
        else:
            answer.append(count)
        
    
    return answer