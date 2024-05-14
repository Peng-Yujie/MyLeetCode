# Graph

## Basic Structure

- **vertice**: node
- **edge**: link between vertices

## Types

- **Directed Graph**: edges have direction
- **Undirected Graph**: edges don't have direction
- **Weighted Graph**: edges have weight

### Directed Graph

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

## Graph Traversal

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
