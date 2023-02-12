user_input = int(input())

wine_amount = list()

for i in range(user_input):
    wine_amount.append(int(input()))

max_sum = list()

max_sum.append(wine_amount[0])
if user_input > 1:
    max_sum.append(max(wine_amount[1], wine_amount[0] + wine_amount[1]))
if user_input > 2:
    max_sum.append(max(wine_amount[0] + wine_amount[2], wine_amount[1] + wine_amount[2], max_sum[1]))

for i in range(3, user_input):
    max_sum.append(max(max_sum[i-2] + wine_amount[i], max_sum[i-3] + wine_amount[i-1] + wine_amount[i], max_sum[i-1]))

print(max_sum[user_input-1])

# 2579번과 다른 점은 반드시 마지막 값이 포함되어야 한다는 조건이 없는 것이다.
