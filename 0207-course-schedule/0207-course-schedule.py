class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = [0] * numCourses
        
        def DFS(a):
            if visited[a] == 1:
                return False
            if visited[a] == 2:
                return True
            visited[a] = 1
            for b in graph[a]:
                if not DFS(b):
                    return False
            visited[a] = 2
            return True
        
        for a in range(numCourses):
            if not DFS(a):
                return False
        
        return True