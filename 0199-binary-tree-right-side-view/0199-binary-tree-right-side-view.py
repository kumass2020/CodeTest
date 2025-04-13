# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append((root, 1))
        dt = defaultdict(list)

        while q:
            node, level = q.popleft()
            dt[level].append(node.val)
            
            for next_node in [node.left, node.right]:
                if next_node:
                    q.append((next_node, level+1))

        answer = []
        for value in dt.values():
            answer.append(value[-1])
        
        return answer