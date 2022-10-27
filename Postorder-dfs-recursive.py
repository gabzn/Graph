graph = {
    'g': ['b', 'f'],
    'a': ['b', 'c'],
    'b': ['c', 'f'],
    'c': ['d'],
    'd': [],
    'e': [],
    'f': ['e']
}

def postorder(graph):
    stack= []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs(node, stack, visited_nodes)

    return stack   
 
def dfs(node, stack, visited_nodes):
    visited_nodes.add(node)
    
    # Visit my children first
    for neighbour in graph[node]:
        if neighbour not in visited_nodes:
            dfs(neighbour, stack, visited_nodes)
    
    # Then visit myself
    stack.append(node) 
