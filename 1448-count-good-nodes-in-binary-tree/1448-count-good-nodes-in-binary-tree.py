# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        def traverse(node, maxx):
            nonlocal answer 

            # if not node.val:
            #     return

            if node.val >= maxx:
                answer += 1
                maxx = node.val

            if node.left:
                traverse(node.left, maxx)
            if node.right:
                traverse(node.right, maxx)

        traverse(root, -100000)
        return answer