N = int(input())
inputs = []
for i in range(0, N):
    inputs.append(int(input()))

zero = []
one = []

# 0 일 때
zero.append(1)
one.append(0)
# 1 일 때
zero.append(0)
one.append(1)

'''
    Solution
    i 번째 항의 값은 (i-1 번째) + (i-2 번째) 와 같다.
    0 의 개수를 저장한 리스트 zero 와 1 의 개수를 저장한 리스트 one 을 개별적으로 취급한다.
'''
for i in range(2, 41):
    zero.append(zero[i-1] + zero[i-2])
    one.append(one[i-1] + one[i-2])

# 각 TestCase 정수에 대하여 0 과 1 의 개수를 공백과 함께 출력 ( 기준 양식 )
for i in inputs:
    print(str(zero[i]) + " " + str(one[i]))