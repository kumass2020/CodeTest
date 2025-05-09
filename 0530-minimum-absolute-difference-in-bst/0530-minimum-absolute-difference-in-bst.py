# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        values = []
        def traverse(node):
            nonlocal min_diff, values

            if not node:
                return
            
            if node.left:
                traverse(node.left)

            if values:
                min_diff = min(min_diff, abs(values[-1]-node.val))
            values.append(node.val)

            if node.right:
                traverse(node.right)
        
        traverse(root)
        return min_diff