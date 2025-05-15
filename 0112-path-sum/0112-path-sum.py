# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # elif not root.left and not root.right and root.val == targetSum:
        #     return True
        
        stack = []
        # is_sum = False

        def traverse(node):
            nonlocal stack
            l = r = False
            
            stack.append(node.val)
            
            if not node.left and not node.right and sum(stack) == targetSum:
                return True
            
            if node.left:
                l = traverse(node.left)
            if node.right:
                r = traverse(node.right)
            
            stack.pop()
            return l or r

        return traverse(root)
            