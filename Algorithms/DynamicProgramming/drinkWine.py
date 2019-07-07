N = int(input())

drink = []
drink.append(0)
for i in range(0, N):
    drink.append(int(input()))

dp = []
dp.append(0)
dp.append(drink[1])
if(N == 1):
    print(dp[N])
    exit()
dp.append(drink[1]+drink[2])
if(N == 2):
    print(dp[N])
    exit()

for i in range(3,N+1):
        dp.append(0)
        dp[i] = max(dp[i-3]+drink[i-1]+drink[i], dp[i-2]+drink[i])
        dp[i] = max(dp[i-1], dp[i])

print(dp[N])