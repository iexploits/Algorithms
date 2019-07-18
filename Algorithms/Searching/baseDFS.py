'''
    DFS [ Stack 개념 활용 ]

'''

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def dfs(graph, root):
    visited = {}
    stack = [root]

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited[curr] = True
            stack.extend(graph[curr])      
    return visited

print(dfs(graph, 'A').keys())
