user_input = int(input())


def continuous_sum(number):
    user_list = list(map(int, input().split()))
    for i in range(1, number):
        user_list[i] = max(user_list[i], user_list[i]+user_list[i-1])
    return max(user_list)


answer = continuous_sum(user_input)
print(answer)