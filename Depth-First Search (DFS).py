def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_vertex)
    print(start_vertex, end=' ')
    
    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
