user_input = int(input())

count_list = [0 for i in range(user_input + 1)]
if user_input > 1:
    count_list[2] = 1
if user_input > 2:
    count_list[3] = 1
    for i in range(4, user_input+1):
        count_list[i] = count_list[i - 1] + 1
        if i % 3 == 0:
            count_list[i] = min(count_list[i], (1+count_list[i//3]))
        if i % 2 == 0:
            count_list[i] = min(count_list[i], (1+count_list[i//2]))

print(count_list[user_input])

