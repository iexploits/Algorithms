N = int(input())

# 입력 처리 : 1~N 째 줄까지의 삼각형의 정수를 동적 배열로 Append.
tri = []
tri.append([])
for i in range(1, N+1):
    tri.append(input().split())

'''
    Solution
    0 째줄의 합 : 0
    1~N 까지 각 요소에 도달할 수 있는 경로들의 합의 최댓값을 구하여 저장.
    현재까지의 최대합 경로는 다음과 같이 나뉠 수 있음.
    1) 시작에 위치한 경우 : 이전 줄 시작( 0 번째 요소 )의 최대합
    2) 끝에 위치한 경우 : 이전 줄 끝( j-1 번째 요소 )의 최대합
    3) 그 사이에 위치한 경우
        : 이전 줄 이전 요소 ( j-1 번째 ) 와 동일 요소 ( j 번째 ) 의 최대합 중 최댓값
    > 위와 같이 현재 도달할 수 있는 경로까지의 최대합 + 자신의 정수를 구해나가면 될 것.

    이를 통해 모든 요소의 최대합을 구했다면, 마지막 열의 최대합들 중 최댓값을 산출해 출력.
'''
dp = []
dp.append([0])
for i in range(1, N+1):
    tmp = []
    for j in range(0, i):
        if j==0 : tmp.append(dp[i-1][0])
        elif j==(i-1) : tmp.append(dp[i-1][j-1])
        else : tmp.append(max(dp[i-1][j-1], dp[i-1][j]))
        tmp[j] = tmp[j] + int(tri[i][j])
    dp.append(tmp)

print(max(dp[N]))