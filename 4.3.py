from collections import deque

def bfs(graph, start_node): 
  
  visited = set()

  queue = deque()

  visited.add(start_node)
  queue.append(start_node)

  while queue:
    m = queue.popleft()
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)
        
  return visited
