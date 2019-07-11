N = int(input())
inputs = list(map(int,input().split()))

dp = []
'''
    Solution 
    - 현재 수 이전의 수들을 보고, 자신보다 작은 수들의 부분수열 길이를 모두 파악.
      그 중에서 가장 큰 부분수열 길이에 1을 더한 것이 나의 최대 부분수열 길이가 될 것.

    - 이중 For 문
        i = 0 ~ N-1 까지 
            j = 0 ~ i-1 까지 ( 내 위치보다 이전에 있는 수 들 )
                if a[j] < a[i] :    ( 내가 더 크다면 )
                    dp[i] = max(dp[i], dp[j])   ( 더 큰 부분수열의 길이로 갱신 ) 
'''     
for i in range(0, N):
    tmp = 0
    for j in range(0, i):
        if inputs[j] < inputs[i]:
            tmp = max(dp[j], tmp)
    dp.append(tmp+1)

print(max(dp))