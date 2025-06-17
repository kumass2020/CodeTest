# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # self.q = deque()
        self.q = []
        self.idx = 0

        def traverse(node):
            if not node:
                # q.append(node)
                return

            if node.left:
                traverse(node.left)

            self.q.append(node)
            
            if node.right:
                traverse(node.right)

        traverse(root)

        self.N = len(self.q)

            


    def next(self) -> int:
        node = self.q[self.idx]
        self.idx += 1

        return node.val
        

    def hasNext(self) -> bool:
        if self.idx > self.N-1:
            return False
        else:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()