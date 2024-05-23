# Bipartite Graph

A graph is bipartite if we can split its set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

Suppose we need to paint every node in the graph using one of two colors, such that **no two adjacent nodes have the same color**. If we can do this, the graph is bipartite.

What is bipartite graph used for?

- Store data that can be divided into two independent sets.
  - For example, films and actors can be divided into two sets.

## Bipartite Graph Check (Traversal)

Basic Graph Traversal:

```python
visited = set()
onPath = []
def traversal(graph, start):
  if start in visited:
    return
  visited.add(start)
  onPath.append(start)  # record the path
  for neighbor in graph[start]:
    traversal(graph, neighbor)

  # do something after visiting all neighbors
  # onPath.pop()
```

To traverse a bipartite graph, we need to assign colors to nodes.

- Paint different color to all neighbors of a node.
- If the neighbor has been visited:
  - Same color: not bipartite.
  - Different color: continue traversal.

```python
class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    visited = {}
    def dfs(node, color):
      if node in visited:
        return visited[node] == color
      visited[node] = color
      return all(dfs(neighbor, 1 - color) for neighbor in graph[node])

    return all(dfs(node, 0) for node in range(len(graph)) if node not in visited)

```
