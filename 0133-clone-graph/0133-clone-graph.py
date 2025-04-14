# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         # copied = Node(1, node.neighbors)
#         # i = 1
#         # cur_node = None
#         # while cur_node.val != node.val:
#         # cur_node = node

#         # print(node)
#         # print(node is True)
#         # print(node is False)
#         # print(node is None)

#         if node is None:
#             return None
#         elif node.neighbors == [[]]:
#             return [[]]

#         visited = set()

#         def traverse(node):
#             if node in visited:
#                 return visited[node]

#             # print(visited)
#             new_node = Node(node.val)
#             visited.add(node)

#             for neighbor in node.neighbors:
#                 # if neighbor not in visited:
                    
#                     new_neighbor = traverse(neighbor)
#                     new_node.neighbors.append(new_neighbor)
            
#             return new_node
        
#         new_node = traverse(node)
#         return new_node


            
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None  

        visited = {}

        def traverse(node):
            if node in visited:
                return visited[node]

            cloned_node = Node(node.val)
            visited[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_node.neighbors.append(traverse(neighbor))

            return cloned_node

        return traverse(node)