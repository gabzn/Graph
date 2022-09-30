Given a undirected graph, find the largest component in this graph.

graph = {
  '0': ['4','7'],
  '1': [],
  '2': [],
  '3': ['6'],
  '4': ['0'],
  '6': ['3'],
  '7': ['0'],
  '8': []
}

def find_size_of_largest_component(graph):
    max_size = 0
    visited_nodes = set()

    for source in graph.keys():
        if source in visited_nodes:
            continue

        max_size = bfs(graph, source, visited_nodes, max_size)

    return max_size

def dfs(graph, source, visited_nodes, max_size):
    current_component_size = 0
    stack = []
    stack.append(source)

    while stack:
        node = stack.pop()
        
        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        current_component_size += 1

        for neighbour in graph[node]:
            stack.append(neighbour)
    
    max_size = max(max_size, current_component_size)
    return max_size

def bfs(graph, source, visited_nodes, max_size):
    current_component_size = 0
    queue = collections.deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        
        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        current_component_size += 1

        for neighbour in graph[node]:
            queue.append(neighbour)
    
    max_size = max(max_size, current_component_size)
    return max_size
