def input_Apartment():
    for i in range(N):
        temp = []
        tmp = str(input())
        for j in range(len(tmp)):
            temp.append(int(tmp[j]))
        area.append(temp)

def isInside(y,x):
    return (0<= y <N) and (0<= x <N)

# BFS 버젼 1 : 자기 자신을 '방문' 하고 시작하는 경우
def BFS(start):
    # 시작 지점 방문 
    queue = [start]
    y, x = start
    visit[y][x] = True
    cnt = 1
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 다음 목적지가 존재하고, 아파트이고, 아직 방문하지 않은 상태라면
            if isInside(ny, nx):
                if area[ny][nx] and not visit[ny][nx]:
                    cnt += 1
                    queue.append([ny,nx])
                    visit[ny][nx] = True
    result.append(cnt)

# BFS 버젼 2 : 자기 자신을 '방문' 하지 않고 시작하는 경우
def BFS_NoVisitCheck(start):
    # 시작 지점 방문 
    queue = [start]
    cnt = 0
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 다음 목적지가 존재하고, 아파트이고, 아직 방문하지 않은 상태라면
            if isInside(ny, nx):
                if area[ny][nx] and not visit[ny][nx]:
                    cnt += 1
                    queue.append([ny,nx])
                    visit[ny][nx] = True
    # 단지에 진입하였으나, 아파트 수가 1개일 경우에 인접한 노드가 없으므로 시작 노드를 예상 방문 ( for 문 ) 불가
    # 그렇기 때문에, 시작하는 집이 있음에도 cnt 값은 증가할 수 없음.
    if cnt is 0 : result.append(1)
    else : result.append(cnt)

def Solve():
    for i in range(N):
        for j in range(N):
            if area[i][j] and not visit[i][j]:
                BFS([i,j])
# 입력 
N = int(input())
area = []
visit = [[False]*N for i in range(N)]
input_Apartment()

result = []

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

Solve()

''' 
    출력
    1. 단지 개수
    2. (만일 단지가 존재한다면) 단지 내 집수를 오름차순으로 정렬 
'''
print(len(result))
if len(result)>0:
    for i in sorted(result):
        print(i)