#-*- coding: utf-8 -*-

# # 입력 처리
N = int(input())
score = []
score.append(0) # 시작지점
for i in range(0,N):
    score.append(int(input()))

# 연산 진행
dp = []
dp.append(0)        # 시작지점
dp.append(score[1]) # 첫번째 칸에서 얻을 수 있는 최대 점수 = 첫번째 칸의 스코어
dp.append(score[1] + score[2]) # 두번째 칸에서 얻을 수 있는 최대 점수 : 1,2 칸 모두 밟았을 경우

'''
    Solution

    규칙 : 3칸 연속으로 오를 수 없음. 
    3칸 이후부터는 점수를 연산할 수 있는 방법이 두 가지로 나뉜다.
    현재 칸에 도달할 때, 
    1) 한 칸 이전을 밟고 온 경우. 그 전 칸을 밟을 수 없으므로 현재 칸으로부터 3칸 전의 최대점수 + 1칸 전 점수 + 현재 칸 점수
    2) 두 칸 이전을 밟고 온 경우, 그 전 칸을 밟았는지에 대한 고려가 필요없으므로 2칸 전의 최대점수 + 현재 칸 점수
'''
for i in range(3, N+1):
    dp.append(max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i]))

print(dp[N])