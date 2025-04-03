# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = []

        if not node:
            return False

        while True:
            if node in visited:
                return True
    
            visited.append(node)

            if node.next:
                node = node.next
            else:
                return False
