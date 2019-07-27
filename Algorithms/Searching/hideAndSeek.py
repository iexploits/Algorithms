def isInside(x):
    return 0 <= x <= 100000

def BFS(start):
    queue = [start]

    while queue:
        now = queue.pop(0)
        if now is K :
            return

        for nxt in (now-1, now+1, now*2) :
            # 더 깊은 깊이 내에서의 탐색에서 방문할 가능성이 존재. 이를 방지하기 위한 트리거 포인트.
            if isInside(nxt) and not dist[nxt]:
                dist[nxt] = dist[now] + 1
                queue.append(nxt)


N, K = map(int, input().split())
# 위치 : 0 ~ 100000
dist = [0] * 100001
BFS(N)
print(dist[K])