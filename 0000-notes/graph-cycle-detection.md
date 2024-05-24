# Graph Cycle Detection

A **cycle** in a **graph** is a non-empty path in which the first and last nodes are the same. A graph is cyclic if it contains a cycle.

## DFS Detection

[x] [LeetCode 207. Course Schedule](../0207-course-schedule/0207-course-schedule.py)

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

## BFS Detection

Consider LeetCode 207. Course Schedule again.

- Find the **in-degree** of each node.
- Add the nodes with **in-degree 0** to the queue.
- Remove the node from the queue and decrease the in-degree of its neighbors.
- If the in-degree of a neighbor becomes 0, add it to the queue.
- If every node is removed from the queue, the graph is acyclic.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        count = 0
        while queue:
            a = queue.popleft()
            count += 1
            for b in graph[a]:
                in_degree[b] -= 1
                if in_degree[b] == 0:
                    queue.append(b)

        return count == numCourses
```

## Topological Sort

[x] [LeetCode 210. Course Schedule II](../0210-course-schedule-ii/0210-course-schedule-ii.py)

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

### DFS

```python
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
```

### BFS

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prerep in prerequisites:
            graph[prerep].append(course)  # from prerep to course
            in_degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            # start with the course without any prerequisite
            if in_degree[course] == 0:
                queue.append(course)

        res = []
        while queue:
            prerep = queue.popleft()
            res.append(prerep)
            for course in graph[prerep]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return res if len(res) == numCourses else []
```
