# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # root = TreeNode(postorder[-1])

        def traverse(inorder, postorder):
            if not inorder:
                return

            val = postorder[-1]
            root_idx = inorder.index(val)
            left = inorder[:root_idx]
            right = inorder[root_idx+1:]

            left_post = postorder[:len(left)]
            right_post = postorder[len(left):len(left)+len(right)]

            node = TreeNode(val)
            node.left = traverse(left, left_post)
            node.right = traverse(right, right_post)

            return node

        root = traverse(inorder, postorder)

        return root