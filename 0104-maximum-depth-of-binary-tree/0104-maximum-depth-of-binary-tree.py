# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        max_depth = 0
        def traverse(node, depth):
            nonlocal max_depth
            # print(depth)
            max_depth = max(max_depth, depth)
            if node.left is not None:
                traverse(node.left, depth+1)
            if node.right is not None:
                traverse(node.right, depth+1)

        if root:
            traverse(root, 1)
        return max_depth if max_depth else 0
            

            