N = int(input())

dp = []
dp.append(0)

for i in range(1, N+1):
    if i==1 : dp.append(1)
    elif i==2 : dp.append(3)
    else : dp.append(dp[i-1] + dp[i-2] * 2)

print(dp[N] % 10007)