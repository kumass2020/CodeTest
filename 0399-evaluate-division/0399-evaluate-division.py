from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (A, B), val in zip(equations, values):
            graph[A].append((B, val))
            graph[B].append((A, 1 / val))
        # print(graph)

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            q = deque()
            q.append((start, 1.0))
            visited = set([start])

            while q:
                node, weight = q.popleft()
                for (nei, w) in graph[node]:
                    if nei in visited:
                        continue
                    new_weight = weight * w
                    if nei == end:
                        return new_weight
                    visited.add(nei)
                    q.append((nei, new_weight))
            return -1.0
        
        results = []
        for C, D in queries:
            results.append(bfs(C, D))
        
        return results
    
        