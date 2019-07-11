N = int(input())
a = []
a = input().split()
a.insert(0, 0)

dp = []
dp.append(-1000)

for i in range(1, N+1):
    tmp = int(a[i])
    dp.append(max(dp[i-1] + tmp, tmp))
print(max(dp))