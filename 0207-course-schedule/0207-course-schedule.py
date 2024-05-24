class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        
        visited = [False] * numCourses
        onPath = [False] * numCourses
        res = False

        def traverse(graph, s):
            nonlocal res
            if onPath[s]:
                res = True
            if visited[s] or res:
                return
            visited[s] = True
            onPath[s] = True
            for t in graph[s]:
                traverse(graph, t)
            onPath[s] = False
        
        for i in range(numCourses):
            traverse(graph, i)
        
        return not res