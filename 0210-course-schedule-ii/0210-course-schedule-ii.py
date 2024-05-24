class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = [0] * numCourses
        res = []

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
            res.append(a)
            return True
        
        for a in range(numCourses):
            if not DFS(a):
                return []
        
        return res