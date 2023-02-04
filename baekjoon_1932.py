user_input = int(input())

integer_triangle = list()
for i in range(user_input):
    integer_triangle.append(list(map(int, input().split())))

for i in range(user_input - 1):
    level = user_input - i - 1
    for j in range(len(integer_triangle[level-1])):
        integer_triangle[level - 1][j] = integer_triangle[level - 1][j] + max(integer_triangle[level][j], integer_triangle[level][j+1])

print(integer_triangle[0][0])