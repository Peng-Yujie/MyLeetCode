class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        def dfs(node, color):
            if node in visited:
                return visited[node] == color
            visited[node] = color
            return all(dfs(neighbor, 1 - color) for neighbor in graph[node])

        return all(dfs(node, 0) for node in range(len(graph)) if node not in visited)