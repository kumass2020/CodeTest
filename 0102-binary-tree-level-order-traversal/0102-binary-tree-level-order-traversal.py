# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        
        q = deque()
        q.append((root))

        answer = []

        while q:
            level_size = len(q)
            temp = []

            # temp.append(node.val)

            # if not q:
            #     answer.append(temp)
            #     temp = []

            # if len(answer) == level+1:
            #     answer[level].append(node.val)
            # else:
            #     answer.append([node.val])

            for i in range(level_size):
                node = q.popleft()

                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            answer.append(temp)

        return answer
