class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import deque
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Undirected graph
            
        # BFS to find path
        visited = [False] * n
        queue = deque([source])
        visited[source] = True
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return False