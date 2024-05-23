class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # buile the graph
        graph = [[] for _ in range(n + 1)]
        for edge in dislikes:
            v, w = edge
            graph[v].append(w)
            graph[w].append(v)

        # check if it is bipartite
        visited = {}
        for node in range(1, n + 1):
            if node in visited:
                continue
            q = deque([(node, 0)])
            while q:
                node, color = q.popleft()
                if node in visited:
                    if visited[node] != color:
                        return False
                    continue
                visited[node] = color
                for neighbor in graph[node]:
                    q.append((neighbor, 1 - color))
        
        return True
