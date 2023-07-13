graph = {
    'g': ['b', 'f'],
    'a': ['b', 'c'],
    'b': ['c', 'f'],
    'c': ['d'],
    'd': [],
    'e': [],
    'f': ['e']
}

# Topological ordering is just the reverse of postorder.
# So, we can just get the postorder and then reverse the list.
def topo_ordering_with_stack(graph):
    stack = []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs_postordering_with_stack(node, graph, stack, visited_nodes)
    
    # Reverse the postorder to obtain the topological order.
    stack.reverse()
    return stack
  
def dfs_postordering_with_stack(node, graph, stack, visited_nodes):
    visited_nodes.add(node)
    
    # Visit my children first
    for neighbour in graph[node]:
        if neighbour not in visited_nodes:
            dfs_postordering_with_stack(neighbour, graph, stack, visited_nodes)
    
    # Then visit myself
    stack.append(node)
---------------------------------------------------------------------------------------------------------------------
def topo_ordering_with_deque(graph):
    queue = deque()
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs_postordering_with_deque(node, queue, visited_nodes)
    
    return queue
  
def dfs_postordering_with_deque(node, queue, visited_nodes):
    visited_nodes.add(node)
    
    # Visit my children first
    for neighbour in graph[node]:
        if neighbour not in visited_nodes:
            dfs_postordering_with_deque(neighbour, queue, visited_nodes)
    
    # Then visit myself
    queue.appendleft(node)
