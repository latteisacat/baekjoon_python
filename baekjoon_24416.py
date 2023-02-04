user_input = int(input())

memo = list(0 for i in range(100))
counter_1 = 0
counter_2 = 0


def fibonacci(number):
    global counter_1
    if number == 1 or number == 2:
        return 1

    else:
        counter_1 += 1
        return fibonacci(number-1) + fibonacci(number - 2)


def fibonacci_with_memo(number):
    global counter_2
    global memo
    if number == 1:
        memo[1] = 1
        return memo[1]
    elif number == 1:
        memo[2] = 1
        return memo[2]
    elif number > 2:
        if memo[number] != 0:
            return memo[number]
        else:
            counter_2 += 1
            memo[number] = fibonacci_with_memo(number-1) + fibonacci_with_memo(number - 2)
            return memo[number]
    else:
        return 0


fibonacci(user_input)
fibonacci_with_memo(user_input)
print(str(counter_1 + 1) + " " + str(counter_2))