import sys
user_input = sys.stdin.readline

input_1 = list(str(user_input()))
input_1.pop()
input_2 = list(str(user_input()))
input_2.pop()
len_1 = len(input_1)
len_2 = len(input_2)

accumulate_list = list(0 for _ in range(len_2))

for i in range(len_1):
    count = 0
    for j in range(len_2):
        if count < accumulate_list[j]:
            count = accumulate_list[j]
        elif input_1[i] == input_2[j]:
            accumulate_list[j] = count + 1

print(max(accumulate_list))

