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
            if not all(DFS(b) for b in graph[a]):
                return False
            visited[a] = 2
            return True
        
        return all(DFS(a) for a in range(numCourses))