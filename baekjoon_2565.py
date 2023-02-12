import sys
user_input = sys.stdin.readline

N = int(user_input())
user_list = list()
for i in range(N):
    user_list.append(list(map(int, user_input().split())))

user_list.sort(key=lambda x: x[0])

sub_list = list(1 for _ in range(N))

for i in range(1, N):
    for j in range(i):
        if user_list[i][1] > user_list[j][1]:
            sub_list[i] = max(sub_list[i], sub_list[j] + 1)

print(N - max(sub_list))
