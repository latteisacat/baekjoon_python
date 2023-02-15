import sys
user_input = sys.stdin.readline

N, K = map(int, user_input().split())

money_value = list()

for i in range(N):
    money_value.append(int(user_input()))

count = 0
for i in range(N):
    if money_value[N - i - 1] <= K:
        count += (K//money_value[N - i - 1])
        K %= money_value[N - i - 1]

print(count)