# 입력 처리
N = int(input())

# 연산 진행
dp = []
dp.append(0)    # 0
dp.append(1)    # 1
dp.append(1)    # 2

# 4 부터 10 까지
for i in range(3,N+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[N])