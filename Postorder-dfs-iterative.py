graph = {
    'g': ['b', 'f'],
    'a': ['b', 'c'],
    'b': ['c', 'f'],
    'c': ['d'],
    'd': [],
    'e': [],
    'f': ['e']
}

def postorder_dfs(graph):
    dfs_stack, ordering = [], []
    visited_nodes = set()

    for node in graph:
        if node in visited_nodes:
            continue

        # Visit all nodes in preorder fashion first.
        preorder = []
        dfs_stack.append(node)
        while dfs_stack:
            cur_node = dfs_stack.pop()
            
            if cur_node in visited_nodes:
                continue
            visited_nodes.add(cur_node)
            
            preorder.append(cur_node)
            
            for neighbour in graph[cur_node]:
                dfs_stack.append(neighbour)

        # After visiting all the neighbours in preorder fashion, we start popping nodes from the end 
        # to simulate that we are visiting all the neighbours first.
        while preorder:
            ordering.append(preorder.pop())

    return ordering
