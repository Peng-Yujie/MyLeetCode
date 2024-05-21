# Basic solution for BFS in Python



from collections import deque


def BFS(start, target) -> int:
  visited = set()
  q = deque()
  
  q.append(start)  # add the start node to the queue
  visited.add(start)
  step = 0  # the number of steps
  
  while q:
    sz = len(q)
    # spread out the nodes
    for i in range(sz):
      cur = q.popleft()
      # check if the current node is the target
      if cur == target:
        return step
      # add the neighbors of the current node to the queue
      for neighbor in cur.neighbors:
        if neighbor not in visited:
          q.append(neighbor)
          visited.add(neighbor)
          
    step += 1  # increment the number of steps
    
  return -1  # return -1 if the target node is not found
      
    