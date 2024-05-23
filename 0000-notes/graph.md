# Graph

## Basic Structure

- **vertice**: node
- **edge**: link between vertices

## Types

- **Directed Graph**: edges have direction
- **Undirected Graph**: edges don't have direction
- **Weighted Graph**: edges have weight

### Directed Graph

#### Table

```python
#  key: vertice
#  value: list of vertices that are connected to the key vertice
graph = {
  0: [1],
  1: [2, 3],
  2: [3],
  3: []
}
```

#### Matrix (2D Array)

```bash
  0 1 2 3
0 0 1 0 0
1 0 0 1 0
2 0 0 0 1
3 1 0 0 0

# Matrix[i][j] = 1 means there is an edge from i to j
```

#### Linked List

create a directed graph using C++ Linked List

```cpp
class Graph {
  private:
    Node* head;
    Node* tail;
  public:
    Graph() {
      head = tail = nullptr;
    }

    void addEdge(int start, int end) {
      Node* newNode = new Node(end);
      if (head == nullptr) {
        head = tail = newNode;
      } else {
        tail->next = newNode;
        tail = newNode;
      }
    }

    void removeEdge(int start, int end) {
      //...
    }
};
```

### Undirected Graph

Undirected graph is actually **bidirectional directed** graph.

#### Table

```python
graph = {
  0: [1],
  1: [0, 2, 3],
  2: [1, 3],
  3: [1, 2]
}
```

#### Matrix

```python
# graph[i][j] == graph[j][i] == 1 means there is an edge between i and j
graph = [
  [0, 1, 0, 0],
  [1, 0, 1, 1],
  [0, 1, 0, 1],
  [0, 1, 1, 0]
]
```

### Weighted Graph (Directed)

#### Table

```python
# graph[x] stores all the neighbors of x and the weight of the edge between x and its neighbors
graph = {
  0: [(1, 10)],
  1: [(2, 20), (3, 30)],
  2: [(3, 40)],
  3: []
}
```

#### Matrix

```python
# graph[i][j] stores the weight of the edge from i to j, 0 means no edge
graph = [
  [0, 10, 0, 0],
  [0, 0, 20, 30],
  [0, 0, 0, 40],
  [0, 0, 0, 0]
]
```

## Graph Traversal

Since graph may contain cycles, we need to keep track of the **visited nodes** to avoid infinite loop.

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

- **Depth First Search (DFS)**
- **Breadth First Search (BFS)**

### DFS

- Starts from the root node and explores as far as possible along each branch
- Returns to the previous node when it reaches a leaf node.
- If the node has been visited, it will not be visited again.
- Stops when all nodes have been visited.

### BFS

Starts from the root node and explores all the neighbor nodes at the present depth prior to moving on to the nodes at
the next depth level.
