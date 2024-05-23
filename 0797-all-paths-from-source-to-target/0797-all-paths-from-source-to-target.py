class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        
        def traverse(graph, node, path):
            path.append(node)

            if node == n - 1:
                res.append(list(path))  # make a copy of path
            
            for v in graph[node]:
                traverse(graph, v, path)
            
            path.pop()
        
        traverse(graph, 0, [])
        return res