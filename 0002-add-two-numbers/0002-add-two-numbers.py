# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if not l1.next:
        #     num1 = 0
        # if not l2.next:
        #     num2 = 0

        # i = 0
        # num1 = 0
        # node = l1
        # while node:
        #     val = node.val
        #     num1 += val * (10**i)
        #     i += 1
        #     node = node.next

        # i = 0
        # num2 = 0
        # node = l2
        # while node:
        #     val = node.val
        #     num2 += val * (10**i)
        #     i += 1
        #     node = node.next

        node1 = l1
        node2 = l2
        #  answer 
        answer = []
        jump = 0
        prev_ans = None
        while node1 or node2:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0

            # if not node1.next and not node2.next:
            #     val3 = (val1 + val2 + jump) // 10
            # else:
            val3 = (val1 + val2 + jump) % 10
            # node3.val = val3
            # cur_ans = ListNode(val3)
            # if prev_ans:
            #     prev_ans.next = cur_ans
            # prev_ans = cur_ans
            # print(val1, val2, val3, jump)
            answer.append(val3)
            jump = (val1 + val2 + jump) // 10

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        if (len(answer) > 1 and jump > 0) or (len(answer) == 1 and l1.val + l2.val >= 10):
            answer.append(1)
        
        node = None
        answer_node = None
        for i in range(len(answer)):
            # print(node)
            if i > 0:
                node.next = ListNode(answer[i])
                node = node.next
            else:
                node = ListNode(answer[i])
                answer_node = node

        return answer_node

