class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)  # v is poorer than u, so v -> u

        answer = [-1] * n

        def dfs(x):
            if answer[x] != -1:
                return answer[x]
            answer[x] = x
            for y in graph[x]:
                candidate = dfs(y)
                if quiet[candidate] < quiet[answer[x]]:
                    answer[x] = candidate
            return answer[x]

        for i in range(n):
            dfs(i)
        return answer
