def isInside(x):
    return 0<= x <= 100000

def BFS(start):
    queue = [start]
    cnt = 0

    while queue:
        now = queue.pop(0)
        for nxt in [now-1, now+1, now*2] :
            if isInside(nxt) and visit[nxt] == False:
                visit[nxt] = True
                if nxt == K :
                    return cnt
                queue.append(nxt)
                cnt += 1


N, K = map(int, input().split())
# 위치 : 0 ~ 100000
visit = [False]*100001
print(BFS(N))