# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # import heapq
        # node = head
        # heap = []
        # while not node:
        #     heapq.heappush(heap, -node.val)
        #     node.next = node

        # answer = []
        # while not heap:
        #     answer.-heapq.heappop(heap)

        if not head:
            return head

        lst = [] 
        node = head
        while node:
            # print(node)
            lst.append([node.val, node])
            node = node.next
        
        lst.sort(key=lambda x: x[0])
        # print(lst)
        # lst[0][1].next=lst[1][1]
        # print(lst[0][1])
        for i in range(1, len(lst)):
            val, node = lst[i]
            prev_val, prev_node = lst[i-1]
            node.next = None
            prev_node.next = node
        
        return lst[0][1]
