graph = {
    'f': ['i', 'g'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

# The only distinction between dfs and bfs is the underlying data structure.
# DFS uses a stack because you want to go deep. By going deep you need to visit the newly appended nodes.
# BFS uses a queue because you want to visit everthing in the order they come in. FCFS.
def directed_has_path_dfs(graph, source, destination):
    #DFS uses a stack
    stack = []
    stack.append(source)
        
    while stack:
        current_node = stack.pop()
        if current_node == destination:
            return True
        
        for neighbour in graph[current_node]:
            stack.append(neighbour)
    
    return False

def directed_has_path_bfs(graph, source, destination):
    #BFS uses a queue
    queue = collections.deque()
    queue.append(source)
    
    while queue:
        current_node = queue.popleft()
        if current_node == destination:
            return True
        
        for neighbour in graph[current_node]:
            queue.append(neighbour)
    
    return False


print(directed_has_path_dfs(graph, 'f', 'k'))
print(directed_has_path_bfs(graph, 'f', 'k'))
