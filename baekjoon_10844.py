user_input = int(input())

number_list = list([0 for i in range(10)] for i in range(user_input))

number_list[0] = list(1 for i in range(10))
number_list[0][0] = 0
if user_input > 1:
    for i in range(1, 10):
        if i == 9:
            number_list[1][i - 1] += number_list[0][i]
        else:
            number_list[1][i-1] += number_list[0][i]
            number_list[1][i+1] += number_list[0][i]

    for i in range(1, user_input - 1):
        for j in range(10):
            if j == 0:
                number_list[i + 1][j + 1] += number_list[i][j]
            elif j == 9:
                number_list[i + 1][j - 1] += number_list[i][j]
            else:
                number_list[i + 1][j + 1] += number_list[i][j]
                number_list[i + 1][j - 1] += number_list[i][j]

print(sum(number_list[user_input-1]) % 1000000000)
