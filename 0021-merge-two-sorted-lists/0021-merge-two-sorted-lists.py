# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return list1
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1

        node1 = list1
        node2 = list2
        new_list = ListNode()
        new_node = new_list
        while True:
            if not node1 and not node2:
                break

            if not node1:
                new_node.next = ListNode(node2.val)
                new_node = new_node.next
                node2 = node2.next
                continue
            if not node2:
                new_node.next = ListNode(node1.val)
                new_node = new_node.next
                node1 = node1.next
                continue
            
            if node1.val <= node2.val:
                new_node.next = ListNode(node1.val)
                new_node = new_node.next
                node1 = node1.next
            else:
                new_node.next = ListNode(node2.val)
                new_node = new_node.next
                node2 = node2.next
        
        return new_list.next

            
