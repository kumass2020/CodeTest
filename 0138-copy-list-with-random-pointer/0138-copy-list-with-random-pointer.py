"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.next)
            node.next = Node(node.val, node.next, node.random)

        def set_random(node):
            if not node:
                return

            if node.random:
                node.random = node.random.next

            if node.next:
                set_random(node.next.next)
        
        def traverse2(node):
            if not node:
                return

            if node.next:
                node.next = node.next.next

            traverse2(node.next)

        traverse(head)
        set_random(head.next)
        traverse2(head.next)

        return head.next

            

        # new_nodes = []
        # idx = 0
        
        # random_map = {} # random_map[node] -> random node
        
        # def traverse(node, new_node):
        #     nonlocal new_nodes, random_map

        #     if not node:
        #         return
            
        #     new_node.next = Node(node.val, None, None)
        #     new_nodes.append((node.random, new_node))
        #     new_node = new_node.next

        #     idx += 1
            
            
        #     if node.next:
        #         traverse(node.next, new_node)

        # def set_random():
        #     nonlocal new_nodes
            
        #     for i in range(len(new_nodes)):
        #         node_random, new_node = new_nodes[i]

        #         if node_random:
        #             new_node.random = new_nodes[idx][1]
            

        
        # root = Node(head.val, None, head.random)
        # traverse(head, root)
        # set_random()

        # return root
            