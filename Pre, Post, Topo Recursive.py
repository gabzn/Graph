# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

graph = {
    'g': ['b', 'f'],
    'a': ['b', 'c'],
    'b': ['c', 'f'],
    'c': ['d'],
    'd': [],
    'e': [],
    'f': ['e']
}

def preorder_dfs(graph):
    dfs_stack = []
    ordering = []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs_stack.append(node)

            while dfs_stack:
                cur_node = dfs_stack.pop()
                
                if cur_node in visited_nodes:
                    continue
                visited_nodes.add(cur_node)

                ordering.append(cur_node)
                
                for neighbour in graph[cur_node]:
                    dfs_stack.append(neighbour)

    return ordering
----------------------------------------------------------------------------------------------------------------------------------------------
Topological ordering is the reverse of postordering.
In order to get topological ordering, just do a normal postordering then reverse the list.

def postorder_dfs(graph):
    stack= []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs_postordering(node, stack, visited_nodes)

    return stack    

def topo_ordering(graph):
    stack= []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs_postordering(node, stack, visited_nodes)
    
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
