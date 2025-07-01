# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        lst = []

        def traverse(node):
            nonlocal lst

            if not node:
                return

            lst.append(node)

            traverse(node.next)
        
        traverse(head)
        
        N = len(lst)
        idx = N-n
        if n == 1:
            lst[idx-1].next = None
        elif n == len(lst):
            head = lst[1]
        else:
            # print(idx, lst)
            lst[idx-1].next = lst[idx+1]
        
        return head