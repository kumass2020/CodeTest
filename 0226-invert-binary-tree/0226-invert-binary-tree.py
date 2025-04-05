# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return root

        def traverse(node):
            # temp = node.left
            # node.left = node.right
            # node.right = temp
            if not node:
                return
            node.left, node.right = node.right, node.left
            
            for next_node in [node.left, node.right]: 
                traverse(next_node)
        
        traverse(root)
        return root