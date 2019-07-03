#-*- coding: utf-8 -*-

# # 입력 처리
N = int(input())
inputs = []
for i in range(0,N):
    inputs.append(int(input()))

# 연산 진행
dp = []
dp.append(0)    # 0
dp.append(1)    # 1
dp.append(2)    # 2
dp.append(4)    # 3

# 점화식 : A[n] = A[n-3] + A[n-2] + A[n-1]
# 4 부터 10 까지
for i in range(4, 11):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

for i in inputs:
    print(dp[i])