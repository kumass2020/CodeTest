# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append((root, 1))     # (node, level)
        
        values = []     # [accum_value, # node]

        while q:
            cur_node, cur_level = q.popleft()

            # if not values[cur_level]:
            if cur_level > len(values):
                values.append([cur_node.val, 1])
            else:
                accum_value, num_nodes = values[cur_level-1]
                accum_value += cur_node.val
                num_nodes += 1
                values[cur_level-1] = [accum_value, num_nodes]

            for next_node in [cur_node.left, cur_node.right]:
                if next_node is not None:
                    q.append((next_node, cur_level+1))

        # print(values)
        answer = []
        for accum_value, num_nodes in values:
            answer.append(accum_value / num_nodes)

        return answer