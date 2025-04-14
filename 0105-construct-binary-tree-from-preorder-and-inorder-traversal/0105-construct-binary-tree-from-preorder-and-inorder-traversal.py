# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def traverse(preorder, inorder):
            if not (preorder or inorder):
                return
            # print(preorder, inorder)
            root = preorder[0]
            root_idx = inorder.index(root)

            new_node = TreeNode(root)

            left = inorder[:root_idx]
            right = inorder[root_idx+1:]

            pre_left = preorder[1:1+len(left)]
            pre_right = preorder[1+len(left):]

            new_node.left = traverse(pre_left, left)
            new_node.right = traverse(pre_right, right)

            return new_node
        
        node = traverse(preorder, inorder)
        return node
