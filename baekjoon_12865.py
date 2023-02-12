import sys
user_input = sys.stdin.readline

N, K = map(int, user_input().split())

stuff_list = list()

value_per_weight = list([0 for _ in range(K+1)] for _ in range(N+1))

stuff_list.append([0, 0])
for i in range(N):
    stuff_list.append(list(map(int, user_input().split())))

# 무게에 맞는 길이의 리스트 생성 후 각 무게에 해당하는 최대 값을 구한다면...? 아 이거 어렵다....

for i in range(1, N+1):
    for j in range(1, K+1):
        stuff_value = stuff_list[i][1]
        stuff_weight = stuff_list[i][0]
        if stuff_weight > j:
            value_per_weight[i][j] = value_per_weight[i - 1][j]
        else:
            value_per_weight[i][j] = max(value_per_weight[i-1][j-stuff_weight] + stuff_value, value_per_weight[i - 1][j])


print(value_per_weight[N][K])


