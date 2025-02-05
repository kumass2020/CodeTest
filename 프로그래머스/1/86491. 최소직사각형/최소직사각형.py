def solution(sizes):
    answer = 0
    final_size_a = 0
    final_size_b = 0
    
    for size_a, size_b in sizes:
        max_size = max(size_a, size_b)
        min_size = min(size_a, size_b)
        
        if max_size > final_size_a:
            final_size_a = max_size
        
        if min_size > final_size_b:
            final_size_b = min_size
    
    answer = final_size_a * final_size_b
        
    
    return answer