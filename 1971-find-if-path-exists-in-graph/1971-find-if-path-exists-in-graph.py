class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(x):
            if x == destination:
                return True 
            if x in visited:
                return False
            visited.add(x)
            
            for i in graph[x]:
                if dfs(i):
                    return True
            return False
        return dfs(source)



        