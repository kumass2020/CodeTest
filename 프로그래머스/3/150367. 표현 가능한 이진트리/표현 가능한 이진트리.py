def solution(numbers):
    answer = []
    
    def is_possible(binary_str):
        if len(binary_str) == 1:
            return True
        
        if binary_str[len(binary_str)//2] == '0':
            if '1' in binary_str:
                return False
            else:
                return True
        else:
            if len(binary_str) > 3:
                pre = binary_str[:len(binary_str)//2]
                post = binary_str[len(binary_str)//2 + 1:]
                
                if not is_possible(pre) or not is_possible(post):
                    return False
            
        return True
                
    
    for number in numbers:
        # 이진수로 변환
        binary_str = ''
        
        num = number
        while num != 0:
            binary_str = str(num % 2) + binary_str
            num = num // 2
        
        # length가 2^i-1이 안되면 왼쪽에 0을 붙여줄 수 있음
        for i in range(1, 64):
            if len(binary_str) < 2 ** i - 1:
                binary_str = '0' * (2 ** i - 1 - len(binary_str)) + binary_str
                break
            elif len(binary_str) == 2 ** i - 1:
                break
        # if len(binary_str) % 2 == 0:
        #     binary_str = '0' + binary_str
        
        # len() 홀수, root가 비면 X
        # 서브 트리도 같은 원리
        if is_possible(binary_str):
            answer.append(1)
        else:
            answer.append(0)
        
    
    return answer