graph = {
    'g': ['b', 'f'],
    'a': ['b', 'c'],
    'b': ['c', 'f'],
    'c': ['d'],
    'd': [],
    'e': [],
    'f': ['e']
}

Topological ordering is just the reverse of postorder.
So we can just can the postorder and then reverse the list.

def topo_ordering(graph):
    stack= []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs_postordering(node, stack, visited_nodes)
    
    # Reverse the postorder to obtain the topological order.
    stack.reverse()
    return stack
  
def dfs_postordering(node, stack, visited_nodes):
    visited_nodes.add(node)
    
    # Visit my children first
    for neighbour in graph[node]:
        if neighbour not in visited_nodes:
            dfs_postordering(neighbour, stack, visited_nodes)
    
    # Then visit myself
    stack.append(node)    
