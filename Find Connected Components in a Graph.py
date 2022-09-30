Given a graph, write a function to find the number of connected components in this graph.

graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}

def find_num_of_connected_components_dfs(graph):
    count = 0
    visited_nodes = set()

    for source in graph.keys():
        if source in visited_nodes:
            continue
        
        # dfs(graph, source, visited_nodes)        
        bfs(graph, source, visited_nodes)
        count += 1

    return count

def dfs(graph, source, visited_nodes):
    stack = []
    stack.append(source)

    while stack:
        node = stack.pop()
        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        for neighbour in graph[node]:
            stack.append(neighbour)

def bfs(graph, source, visited_nodes):
    queue = collections.deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        for neighbour in graph[node]:
            queue.append(neighbour)

print(find_num_of_connected_components_dfs(graph))
