from collections import Counter
def solution(topping):
    answer = 0
    
    counts_B = dict(Counter(topping))
    counts_A = {}
    # print(counts_B)
    # print(dict.__doc__)
    
    for i in range(len(topping)):
        # print(counts_A.keys(), counts_B.keys(), len(counts_B))
        val = topping[i]
        counts_A[val] = counts_A.get(val, 0) + 1
        counts_B[val] = counts_B.get(val, 0) - 1
        
        if counts_B.get(val) == 0:
            # counts_B.del(val)
            del counts_B[val]
        
        if len(counts_A) == len(counts_B):
            answer += 1
    
    return answer