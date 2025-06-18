# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        start_node = None
        end_node = None
        
        def traverse(node, node_prev):
            nonlocal left, right, lst, start_node, end_node

            if not node:
                return
            
            # print(node.val)

            if left <= node.val <= right:
                lst.append(node)
                
                if node_prev and node_prev.val < left:
                    start_node = node_prev
            
            if not end_node and node.next and node.next.val > right:
                end_node = node.next

            traverse(node.next, node)

        traverse(head, None)

        for i in range(len(lst)-1, -1, -1):
            node = lst[i]

            # print(node.val)
            if i-1 >= 0:
                node.next = lst[i-1]

        # print(start_node)
        # print(end_node)

        if lst:
            if start_node:
                start_node.next = lst[-1]
            if end_node:
                lst[0].next = end_node

        # print(start_node)
        # print(head)

        return head

            
            # if node.next and left <= node.val <= node.next.val <= right:
            #     if node_prev:
            #         node_prev.next = node.next
            #     node.next.next = node



            # node_prev = node

