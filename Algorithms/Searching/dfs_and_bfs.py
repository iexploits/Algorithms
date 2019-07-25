'''
    BOJ 1260 - DFS 와 BFS
    
    DFS [ Stack 개념 활용 ]
    BFS [ Queue 개념 활용 ] 

    # 예외처리
    - 더이상 갈 곳이 없다면 순회 종료.
     > 만약 주어진 간선들이 시작 노드와는 연결 안되어있다면 ? 시작 노드만 출력하고 바로 종료해야함.
'''

graph = {}

def input_Graph(M):
    for i in range(0, M):
        Start, End = map(int, input().split())
        if Start not in graph:
          graph[Start] = set([])
        if End not in graph:
          graph[End] = set([])
        graph[Start].add(End)
        graph[End].add(Start)

def dfs(root):
    if root not in graph:
        print(root)
        return
    visited = []
    stack = [root]

    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            # Reverse = True 옵션을 통해 작은 순서대로 탐색
            ''' 
                차집합 개념 활용 : 현재 뽑아놓은 노드 이후에 방문할 노드들 ( graph[curr] ) 에서 
                                visited 를 차집합 연산. 즉 이미 방문한 노드가 있다면 빼버려야함.
            '''
            stack.extend(sorted(list(graph[curr] - set(visited)), reverse=True))      
    result = list(map(str,visited))
    Search_Printer(result)

def bfs(root):
    if root not in graph:
        print(root)
        return
    visited = []
    queue = [root]

    while queue:
        # Queue : FIFO ( 선입 선출 ) 이므로 0번째 요소를 pop() 해야함.
        curr = queue.pop(0)
        if curr not in visited:
            visited.append(curr)
            queue.extend(sorted(list(graph[curr] - set(visited))))
    result = list(map(str,visited))
    Search_Printer(result)

def Search_Printer(result):
    print(" ".join(result))

N, M, V = map(int, input().split())

# Graph 입력 받기
input_Graph(M)

dfs(V)
bfs(V)