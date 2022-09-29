# Instead of given a graph directly, we are given the edges that connect the nodes.
# In this scenerio, we need to constructure the graph on our own.
edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

# A helper function to convert edges into an adjacency list AKA graph.
def convert_edges_to_graph(edges):
    graph = collections.defaultdict(list)

    for edge in edges:
        node_a, node_b = edge
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    
    return graph 

# Undirected graphs might contain cycles. We need to prevent the case we are visiting a node again and again.
# To prevent we run into a cycle, we use a set to record every node that we visit.
# If a node already in the set, that means it's been visited and you can't get the answer by visiting this node again.
# So, we just go to the next iteration.
def undirected_has_path_dfs(edges, source, destination):
    graph = convert_edges_to_graph(edges)
    visited_nodes = set()

    stack = []
    stack.append(source)
    
    while stack:
        node = stack.pop()
        if node in visited_nodes:
            continue
        visited_nodes.add(node)
        
        if node == destination:
            return True
            
        for neighbour in graph[node]:
            stack.append(neighbour)
    
    return False 

def undirected_has_path_bfs(edges, source, destination):
    graph = convert_edges_to_graph(edges)
    visited_nodes = set()

    queue = collections.deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        if node in visited_nodes:
            continue
        visited_nodes.add(node)
        
        if node == destination:
            return True

        for neighbour in graph[node]:
            queue.append(neighbour)

    return False

print(undirected_has_path_dfs(edges, 'j', 'm'))
print(undirected_has_path_bfs(edges, 'i', 'o'))
