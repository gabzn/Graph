Given a DAG, return one of the topological orderings of this graph.

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

def topo_sort(graph):
    stack= []
    visited_nodes = set()

    for node in graph:
        if node not in visited_nodes:
            dfs(node, stack, visited_nodes)
    
    # topo_ordering = []
    # while stack:
    #     topo_ordering.append(stack.pop())

    stack.reverse()
    return stack

def dfs(node, stack, visited_nodes):
    visited_nodes.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited_nodes:
            dfs(neighbour, stack, visited_nodes)
    
    stack.append(node)
