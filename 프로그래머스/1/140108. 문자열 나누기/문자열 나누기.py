def solution(s):
    answer = 0
    
    # s_list = s.split("")
    
    x_count = 0
    other_count = 0
    
    for i, character in enumerate(s):
        if x_count == 0:
            answer += 1
            x = character
        
        if character == x:
            x_count += 1
        else:
            other_count += 1
        
        if x_count == other_count:
            x_count = 0
            other_count = 0
            # answer += 1
        
        
        # if i != len(s)-1:
        #     for other_char in s[i+1:]:
        #         if other_char != x:
        #             other_count += 1
        #         if other_char == 
                
            
    
    return answer