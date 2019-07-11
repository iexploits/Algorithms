N = int(input())

dp = []
dp.append([])

for i in range(1, N+1):
    tmp = []
    if i == 1 :
        dp.append([1,1,1,1,1,1,1,1,1,1])
    else :
        # 제일 큰 자릿수가 0 일 때
        tmp.append(dp[i-1][1])

        for j in range(1, 9):
            tmp.append(dp[i-1][j-1] + dp[i-1][j+1])

        # 제일 큰 자릿수가 9
        tmp.append(dp[i-1][8])

        dp.append(tmp)

sum = 0
# 0 으로 시작하는 수는 카운트 x, 1~9 로 시작하는 수만 카운트할 것.
for i in range(1, 10):
    sum = sum + dp[N][i]

print(sum%1000000000)