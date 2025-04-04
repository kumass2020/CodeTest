from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            print(stack)
            if stack and mapping.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            
        if stack:
            return False
        else:
            return True


