N = int(input())

drink = []
drink.append(0)
for i in range(0, N):
    drink.append(int(input()))

dp = []
dp.append(0)

'''
    Solution
    포도주를 3잔 이상 연달아 마실 수 없기 때문에 총 2가지 경우를 생각해볼 수 있다.
    또한 계단오르기 문제와는 다르게 마지막 잔을 꼭 마실 필요가 없다.
    1. 포도주가 1잔, 2잔 주어진 경우 
        - 포도주를 모두 마신 것이 최대량
    2. 포도주가 3잔 이상 주어진 경우 
        - 1) 2잔 전까지의 최대 + 현재 포도주 마심
          2) 3잔 전까지의 최대 + 이전 포도주 + 현재 포도주 마심
          3) 현재 포도주 안 마심 ( 이전 잔 까지의 마신 값이 최대일 경우 )
'''
for i in range(1,N+1):
    if(i == 1):
        dp.append(drink[1])
        continue
    if(i == 2):
        dp.append(drink[1] + drink[2])
        continue
    dp.append(0)
    dp[i] = max(dp[i-3]+drink[i-1]+drink[i], dp[i-2]+drink[i])
    dp[i] = max(dp[i-1], dp[i])
print(dp[N])