Given a set of edges, find the shortest path between 2 nodes. The shortest path means the shortest distance between source and destination
# Shortest path uses bfs!!!!! A queue!!!!

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
shortestPath(edges, 'a', 'e') // -> 3
shortestPath(edges, 'e', 'c') // -> 2

def convert_edges_to_graph(edges):
    graph = collections.defaultdict(list)

    for edge in edges:
        node_a, node_b = edge
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    return graph

def shortest_path(edges, source, destination):
    # Shortest path uses bfs
    graph = convert_edges_to_graph(edges)
    visited_nodes = set()    

    # To find the shortest path between source and destination,
    # we need to keep track of the distance of the current node from the source node.
    # The source node has a distance of 0 to itself.
    # The neighbours of source have a distance of 0 + 1 and so on.
    queue = collections.deque()
    queue.append((source, 0))

    while queue:
        node, distance_from_source = queue.popleft()

        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        if node == destination:
            return distance_from_source
        
        # We can update the distance by doing distance_from_source += 1 and push it to the queue.
        distance_from_source += 1
        for neighbor in graph[node]:
            queue.append((neighbor, distance_from_source))

    return -1
