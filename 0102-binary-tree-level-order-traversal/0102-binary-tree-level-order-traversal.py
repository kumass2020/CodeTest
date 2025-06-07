# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        
        q = deque()
        q.append((root, 0))

        answer = []

        while q:
            node, level = q.popleft()

            if len(answer) == level+1:
                answer[level].append(node.val)
            else:
                answer.append([node.val])

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        return answer
