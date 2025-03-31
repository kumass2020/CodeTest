def solution(s):
    answer = []
    
    counter = 1
    zero_counter = 0
    
    while True:
        new_s = ''
        for char in s:
            if char == '1':
                new_s += '1'
        # counter += 1
        zero_counter += (len(s) - len(new_s))
        s = new_s
        
        if s == '1':
            break
        
        new_s = ''
        s_len = len(s)
        while True:
            num = s_len % 2
            s_len = s_len // 2
            new_s = str(num) + new_s

            if s_len == 0:
                break
        counter += 1
        # zero_counter += (len(s) - len(new_s))
        s = new_s
        
        if s == '1':
            break
    
    return [counter, zero_counter]