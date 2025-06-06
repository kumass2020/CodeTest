# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        idx = 0
        answer = None
        def traverse(node):
            nonlocal idx, answer, k

            if not node or answer:
                return
            
            if node.left:
                traverse(node.left)
            idx += 1
            if idx == k:
                answer = node.val

            if node.right:
                traverse(node.right)

        traverse(root)
        return answer