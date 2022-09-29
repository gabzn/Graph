graph = {
    'f': ['i', 'g'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

def has_path_dfs(graph, source, destination):
    #DFS uses a stack
    stack = []
    stack.append(source)

    while stack:
        current_node = stack.pop()
        print(current_node)
        if current_node == destination:
            return True
        
        for neighbour in graph[current_node]:
            stack.append(neighbour)
    
    return False

def has_path_bfs(graph, source, destination):
    #BFS uses a queue
    queue = collections.deque()
    queue.append(source)

    while queue:
        current_node = queue.popleft()
        print(current_node)
        if current_node == destination:
            return True
        
        for neighbour in graph[current_node]:
            queue.append(neighbour)
    
    return False


print(has_path_dfs(graph, 'f', 'k'))
print(has_path_bfs(graph, 'f', 'k'))
