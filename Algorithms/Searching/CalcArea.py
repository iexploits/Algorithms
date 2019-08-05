from collections import deque

def isInside(y,x):
    return (0<= y < M) and (0<= x < N)

def fillArea():
    # start y,x -> end y,x
    sx, sy, ex, ey = map(int, input().split())

    for i in range(sy, ey):
        for j in range(sx, ex):
            area[i][j] = 1

def BFS(start):
    y, x = start
    queue = deque()
    queue.append(start)

    area[y][x] = 1
    cnt = 1
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if isInside(ny, nx):
                if area[ny][nx] is 0:
                    cnt += 1
                    area[ny][nx] = 1
                    queue.append([ny, nx])
    result.append(cnt)

# N : 가로,  M : 세로
M, N, K = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
area = [[0]*N for i in range(M)]
result = []

for i in range(K):
    fillArea()

for i in range(M):
    for j in range(N):
        if area[i][j] is 0:
            BFS([i, j])

print(len(result))
print(" ".join(map(str,sorted(result))))