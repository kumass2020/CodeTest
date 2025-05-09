# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        prev = None
        stack = [root]

        while stack:
            cur = stack.pop()

            if prev:
                prev.left = None
                prev.right = cur
            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
            prev = cur

        # new_node = TreeNode(val=root.val)

        # def traverse(node, new_node):
        #     if not node:
        #         return
            
        #     print(node.val, new_node)
        #     # new_node.right = TreeNode(val=node.val)
            
        #     if node.left:
        #         new_node.right = traverse(node.left, new_node.right)
        #     if node.right:
        #         new_node.right = traverse(node.right, new_node.right)

        #     return TreeNode(val=node.val)
            
        # traverse(root, new_node)
        # root = new_node

        # new_node = TreeNode(val=root.val)
        # new_node_root = new_node
        # def traverse(node):
        #     nonlocal new_node

        #     if not node:
        #         return

        #     new_node.right = TreeNode(val=node.val)
        #     new_node = new_node.right
            
        #     if node.left:
        #         traverse(node.left)
        #     if node.right:
        #         traverse(node.right)


        # traverse(root)
        # root = new_node_root