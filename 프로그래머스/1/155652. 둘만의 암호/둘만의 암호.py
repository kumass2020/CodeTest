def solution(s, skip, index):
    answer = ''
    skip_list = []
    
    for elem in skip:
        skip_list.append(ord(elem))
    
    for i, character in enumerate(s):
        idx = ord(character)
        for j in range(index):
            idx += 1
            
            if idx > 122:
                idx = 96 + (idx - 122)
            
            while idx in skip_list:
                idx += 1
                
                if idx > 122:
                    idx = 96 + (idx - 122)
        answer += chr(idx)
    return answer