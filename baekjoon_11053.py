user_input = int(input())

user_list = list(map(int, input().split()))

sub_list = list(1 for i in range(user_input))

for i in range(1, user_input):
    for j in range(i):
        if user_list[i] > user_list[j]:
            sub_list[i] = max(sub_list[i], sub_list[j]+1)

print(max(sub_list))

