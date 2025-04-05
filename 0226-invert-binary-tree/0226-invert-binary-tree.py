# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # node = root
        def traverse(node):
            # while node.left or node.right:
            # if node.left and node.right:
            temp = node.left
            node.left = node.right
            node.right = temp
            # elif node.left and not node.right:
            #     node.right = node.left
            # elif not node.left and node.right:
            #     node.left = node.right
            
            for next_node in [node.left, node.right]:
                if next_node:
                    traverse(next_node)
        if root:
            traverse(root)
        else: 
            return None
        return root