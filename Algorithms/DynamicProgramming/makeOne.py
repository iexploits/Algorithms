#-*- coding: utf-8 -*-

n = int(input())
a = []

a.append(0) 
a.append(0)

for i in range(2, n+1):
    # [i-1] 의 연산회수와 [i//3], [i//2] 의 최소값중 비교
    a.append(a[i-1])
    if i%2 == 0:
        a[i] = min(a[i//2], a[i])
    if i%3 == 0:
        a[i] = min(a[i//3], a[i])
    # 채택된 최소 연산회수에 1을 더한 것이 i 의 연산회수가 될 것
    a[i] = a[i] + 1

print(a[n])