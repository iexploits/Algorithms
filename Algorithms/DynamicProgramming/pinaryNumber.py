# 입력 처리
N = int(input())

# 연산 진행
dp = []
dp.append(0)    # 0
'''
    Solution
    이친수의 경우는 다음과 같다.
    1 ) 1
    2 ) 10
    3 ) 100, 101
    4 ) 1000, 1001, 1010
    이는 N-1 자릿수들에 0을 붙인 것과 N-2 자릿수들에 01 을 붙인 경우의 수를 모두 센 것과 같다.
    그러므로 점화식 : A[n] = A[n-1] + A[n-2]
'''
for i in range(1, N+1):
    if i == 1 or i == 2 : dp.append(1)
    else : dp.append(dp[i-1] + dp[i-2])

print(dp[N])