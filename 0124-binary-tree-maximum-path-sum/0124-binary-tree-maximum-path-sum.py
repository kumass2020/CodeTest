# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def traverse(node):
            nonlocal max_sum

            if not node:
                return 0

            left_gain = max(traverse(node.left), 0)
            right_gain = max(traverse(node.right), 0)

            max_sum = max(max_sum, left_gain+node.val+right_gain)   # 현재 node가 root가 되는 경우

            return node.val + max(left_gain, right_gain)

        traverse(root)
        return max_sum
        
        # def traverse(node):
        #     center = node.val

        #     left_node = node.left
        #     total_left = 0
        #     while left_node:
        #         val1 = left_node.left.val if left_node.left else 0
        #         val2 = left_node.right.val if left_node.right else 0
                
        #         if val1 > val2:
        #             total_left += val1
        #             left_node = left_node.left
        #         else:
        #         left_node
            
        #     right = node.right
        #     total_right = 0
        #     while right_node:
        #         val1 = right_node.left.val if right_node.left else 0
        #         val2 = right_node.right.val if right_node.right else 0
        #         total_right += max(val1, val2)

        #     # 만약 left + center나 right + center가 음수면 center 탈락
        #     if center + total_left < 0 and center + total_right < 0:
        #         return center
        #     elif center + total_left < 0:
        #         return traverse(node.right)
        #     elif center + total_right < 0:
        #         return traverse(node.left)
        #     else:
        #         return total_left + center + total_right

        # return traverse(root)
            
