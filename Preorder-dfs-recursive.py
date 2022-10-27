graph = {
    'g': ['b', 'f'],
    'a': ['b', 'c'],
    'b': ['c', 'f'],
    'c': ['d'],
    'd': [],
    'e': [],
    'f': ['e']
}

def preorder(graph):
    stack= []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs(node, stack, visited_nodes)
    
    return stack

def dfs(node, stack, visited_nodes):
    visited_nodes.add(node)
    
    # Visit myself first
    stack.append(node)    
    
    # Then visit my children
    for neighbour in graph[node]:
        if neighbour not in visited_nodes:
            dfs(neighbour, stack, visited_nodes)
