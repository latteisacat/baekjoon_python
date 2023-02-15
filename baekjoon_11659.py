import sys
user_input = sys.stdin.readline

N, M = map(int, user_input().split())

number_list = list(map(int, user_input().split()))

temp = 0

sum_list = [0]

for i in number_list:
    temp += i
    sum_list.append(temp)

for k in range(M):
    i, j = map(int, user_input().split())
    print(sum_list[j] - sum_list[i-1])

# 이 문제는 그냥 구현하면 시간 초과가 뜬다...
# 리스트에 0부터 특정 구간까지의 합을 미리 저장해놓고 꺼내서 계산하는 식으로 해야 시간초과가 뜨지 않는다.
# ex)구간 2~9 까지의 합은? 0~9 - 0~1
