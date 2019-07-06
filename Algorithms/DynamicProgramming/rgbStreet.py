N = int(input())

price = []
price.append([0,0,0])       # N = 0 일 때 : 빈 배열
for i in range(0,N) :
    p = input().split()
    
    price.append(p)

dp = []
dp.append([0, 0, 0])        # N = 0 일 때 : 빈 배열
'''
    Solution

    i 번째 줄의 집을 칠 했을 때 각 최소연산을 생각해보면
    1) R 선택 ( 앞집 : G or B )         
    2) G 선택 ( 앞집 : R or B )         
    3) B 선택 ( 앞집 : R or G )         

    # 이를 종합해보면, 이전 줄의 집에 칠한 색 (j+1)%2 , (j+2)%2 중 최솟값을 선택한다는 것을 알 수 있음.
    이렇게 구한 이전 집의 최소가격에 현재 줄의 색 가격을 더해 저장하며 Bottom-Up 방식으로 N까지 연산한다.
'''
for i in range(1, N+1) :  # 1~N 까지 반복
    tmp = []
    for j in range(0, 3) :  # 0~2 : Red, Green, Blue 의 각 Price
        tmp.append(min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + int(price[i][j]))
    dp.append(tmp)

result = min(dp[N])

print(result)