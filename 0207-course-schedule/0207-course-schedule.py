class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #You are given a graph
        #it is one diractional and under numCourses return true
        #else return false [ then <- first]
        Map = defaultdict(list)
        for a,b in prerequisites :
            Map[a].append(b)
        state = [0]*numCourses
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for neighbour in Map[course]:
                if not dfs(neighbour):
                    return False
            state[course] = 2
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        