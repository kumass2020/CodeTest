"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dt = {}

        def traverse(node, level):
            if not node:
                return

            if dt.get(level):
                dt[level].next = node
            dt[level] = node
            
            traverse(node.left, level+1)
            traverse(node.right, level+1)

        
        traverse(root, 0)

        for key, value in dt.items():
            dt[key].next = None
        
        return root