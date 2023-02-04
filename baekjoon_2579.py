user_input = int(input())

stair = list()

for i in range(user_input):
    stair.append(int(input()))

max_sum = list()

max_sum.append(stair[0])
if user_input > 1:
    max_sum.append(max(stair[0]+stair[1], stair[1]))
if user_input > 2:
    max_sum.append(max(stair[0]+stair[2], stair[1]+stair[2]))

for i in range(3, user_input):
    max_sum.append(max(max_sum[i-2]+stair[i], max_sum[i-3]+stair[i-1]+stair[i]))

print(max(max_sum))
