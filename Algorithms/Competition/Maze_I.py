from collections import deque

def Input():
    for i in range(N):
        temp = []
        tmp = str(input())
        for j in range(len(tmp)):
            temp.append(tmp[j])
        maze.append(temp)

def isInside(y, x):
    return (0<= y <N) and (0<= x <M)

def BFS(root):
    visit = [[False]*M for i in range(N)]

    y, x = root
    visit[y][x] = True
    queue = deque()
    queue.append(root)
    
    while(queue):
        y, x = queue.popleft()
        c = maze[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if c is 'U' and i is 0:
                continue
            elif c is 'R' and i is 1:
                continue
            elif c is 'D' and i is 2:
                continue
            elif c is 'L' and i is 3:
                continue
            
            if isInside(ny,nx):
                if visit[ny][nx] is False:
                    queue.append([ny,nx])
                    visit[ny][nx] = True
    for i in visit:
        print(i)
    
    
    

N, M, Q = map(int, input().split())

maze = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

Input()
BFS([1,1])