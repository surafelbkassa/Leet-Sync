class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #You are given a graph
        #it is one diractional and under numCourses return true
        #else return false [ then <- first]
        graph = {i : [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
        """
        graph = {
            0:[],
            1:[0]
        }
        """
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if graph[course] == []:
                return True
            visiting.add(course)
            for b in graph[course]:
                if not dfs(b):
                    return False
            visiting.remove(course)
            graph[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
