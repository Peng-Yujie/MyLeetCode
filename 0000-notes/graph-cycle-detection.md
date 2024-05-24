# Graph Cycle Detection

A **cycle** in a **graph** is a non-empty path in which the first and last nodes are the same. A graph is cyclic if it contains a cycle.

## DFS Detection

[x] LeetCode 207. Course Schedule

To handle a prerequisite problem, we can consider it as a **directed graph**. If there is a cycle in the graph, the prerequisites are not valid.

- The courses are represented by nodes.
- The prerequisites are represented by edges.
- If you must take course B before course A, the edge is from B to A.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      graph = [[] for _ in range(numCourses)]
      for course, prereq in prerequisites:
        graph[course].append(prereq)

      visited = [0] * numCourses
      def dfs(course):
        if visited[course] == 1:
          return False
        if visited[course] == 2:
          return True
        visited[course] = 1
        for prereq in graph[course]:
          if not dfs(prereq):
            return False
        visited[course] = 2
        return True

      for course in range(numCourses):
        if not dfs(course):
          return False
      return True

```

# Topological Sort

[ ] LeetCode 210. Course Schedule II

**topological sort** will flatten the graph into a linear order.

Suppose the graph is like this:

```python
graph = [
  [1, 2],
  [3],
  [3],
  []
]
```

Then the topological sort is `[0, 1, 2, 3]` or `[0, 2, 1, 3]`.
