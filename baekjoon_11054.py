user_input = int(input())

user_list = list(map(int, input().split()))

sub_list = list(1 for i in range(user_input))

for i in range(1, user_input):
    for j in range(i):
        if user_list[i] > user_list[j]:
            sub_list[i] = max(sub_list[i], sub_list[j]+1)


for i in range(1, user_input):
    for j in range(i):
        if user_list[i] < user_list[j]:
            sub_list[i] = max(sub_list[i], sub_list[j] + 1)

print(max(sub_list))

# import sys
# user_input = sys.stdin.readline
#
# def binary_search(r, target):
#     start, end = 0, len(r)
#
#     while start < end:
#         mid = (start + end) // 2
#         if r[mid] >= target:
#             end = mid
#         else:
#             start = mid + 1
#     return start
#
# def lis(num):
#     dp = [0 for _ in range(n)]
#     dp[0] = 1
#     r = [num[0]]
#
#     for i in range(1, n):
#         if num[i] > r[-1]:
#             r.append(num[i])
#         else:
#             r[binary_search(r, num[i])] = num[i]
#         dp[i] = len(r)
#
#     return dp
#
# n = int(user_input())
# num = list(map(int, user_input().split()))
# answer = 1
#
# asc = lis(num)
# print(asc)
# des = lis(num[::-1])
# print(des)
# des = des[::-1]  # 처음부터 끝까지 -1칸 간격(역순) 으로 접근하라는 뜻
# print(des)
#
# for i in range(n - 1):
#     answer = max(answer, asc[i] + des[i] - 1)
#
# print(answer)