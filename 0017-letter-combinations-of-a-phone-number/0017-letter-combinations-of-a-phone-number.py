class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]
        
        L = len(digits)
        answer = []
        comb = ''
        visited = [0 for i in range(L)]
        def dfs(idx, comb, visited):
            nonlocal answer
            # for i in range(idx, len(digits)):
            if len(comb) == L:
                answer.append(comb)
            else:
                for i in range(idx, L):
                    # idx = int(digit)-2
                    digit = digits[i]
                    letter_idx = int(digit)-2
                    for letter in letters[letter_idx]:
                        if not visited[i]:
                            visited[i] = 1
                            comb += letter
                            dfs(idx+1, comb, visited)
                            comb = comb[:-1]
                            visited[i] = 0
        dfs(0, '', visited)

        return answer if digits else []

