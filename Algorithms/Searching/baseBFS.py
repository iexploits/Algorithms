'''
    BFS [ Queue 개념 활용 ]
    
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

def bfs(graph, root):
    visited = {}
    queue = [root]

    while queue:
        # Queue : FIFO ( 선입 선출 ) 이므로 0번째 요소를 pop() 해야함.
        curr = queue.pop(0)
        if curr not in visited:
            visited[curr] = True
            queue.extend(graph[curr])
    return visited

print(bfs(graph, 'A').keys())