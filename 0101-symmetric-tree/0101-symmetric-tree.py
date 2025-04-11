# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            pass
        elif bool(root.left) ^ bool(root.right):
            return False
        else:
            return True

        

        
        # def traverse(node, is_left):
            
            # if is_left:
            #     if node.left:
            #         traverse(node.left, is_left)
            #     if node.right:
            #         traverse(node.right, is_left)
            # else:
            #     if node.right:
            #         traverse(node.right, is_left)
            #     if node.left:
            #         traverse(node.left, is_left)

        def traverse(node1, node2):
            print(node1, node2)
            # if not node1.left and not node1.right and not node2.left and not node2.right:
            #     return True

            if node1.val != node2.val:
                return False

            if bool(node1.left) ^ bool(node2.right):
                return False
            if bool(node1.right) ^ bool(node2.left):
                return False

            if node1.left and node2.right:
                if not traverse(node1.left, node2.right):
                    return False
            
            if node1.right and node2.left:
                if not traverse(node1.right, node2.left):
                    return False
            
            return True
        
        return True if traverse(root.left, root.right) else False
        


