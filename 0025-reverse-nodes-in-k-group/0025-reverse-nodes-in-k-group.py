# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next or k == 1:
            return head

        
        def traverse(node, prev):
            nonlocal k

            if not node:
                return
            
            temp = node
            for i in range(k-1):
                if temp.next:
                    temp = temp.next

                    if i == k-2:
                        if temp.next:
                            last = temp.next
                        else:
                            last = None
                else:
                    return
            
            cur = node
            temp = cur.next
            for i in range(k-1):
                if temp.next:
                    temp2 = temp.next
                else:
                    temp2 = None

                temp.next = cur
                
                if k == 0:
                    cur.next = temp2

                cur = temp
                temp = temp2

            prev.next = cur
            node.next = last
            prev = node

            traverse(last, prev)

        dummy = ListNode(0, next=head)
        traverse(head, dummy)
        
        return dummy.next

            # for i in range(k-1):
            #     if cur.next:                    
            #         temp = cur.next
            #     else:
            #         temp = None

            #     cur.next.next = cur

            #     if temp.next:
            #         cur.next = temp.next

            #     if i == k-2:
            #         prev = temp.next
            #         return

            #     # if temp:
            #     #     temp = temp.next
            #     # else:
            #     #     return

            #     cur = node.next


