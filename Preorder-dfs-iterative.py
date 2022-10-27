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
    dfs_stack, ordering = [], []
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
