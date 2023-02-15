
def get_suffix_arr(input_string):
    n = len(input_string)
    t = 1
    group = list(0 for _ in range(n+1))
    group[n] = -1

    suffix_arr = list()
    for j in range(n):
        group[j] = ord(input_string[j])

    for k in range(n):
        suffix_arr.append(k)

    while t < n:
        suffix_arr.sort(key=lambda x: (group[x], group[min(x+t, n)]))
        # 이 부분이 오류가 난다는 점에서 c++과 파이썬간의 차이가 약간 보였다.
        # c++의 compare함수를 보면
        #     bool comp(int i, int j) {
        #       if (group[i] != group[j])
        #          return group[i] < group[j];
        #       return group[i + t] < group[j + t];
        #     }
        # 첫 반복의 경우 그룹이 전부 다르기 때문에 i+t를 마주칠 일이 없다.
        # 어차피 suffix_arr의 값들은 group의 인덱스 내 이므로 + t를 하지 않는다면 ouf of index 에러가 발생할 이유가 없다.
        # 마지막 group 값은 항상 -1 이므로 임의의 누군가와 같아질 수 없기에 index 밖의 값을 참조할 일이 없어보인다.
        # 실제로 c++에서는 i+t 와 j+t가 index 값을 넘어가도 out of index 에러가 나지 않는 모습을 볼 수 있다.
        # 그러나 파이썬은 일단 t를 집어넣어 무슨 값인지 확인 후 진행하는 것으로 보인다.
        # 따라서 앞의 조건인 group[x]를 통과하지 못할 상황임에도 일단 group[x+t]가 무슨 값인지 확인하게되고, out of index 에러가 나는 것이다.

        new_group = list(0 for _ in range(n+1))
        new_group[suffix_arr[0]] = 0
        new_group[n] = -1

        for i in range(1, n):
            p, q = suffix_arr[i-1], suffix_arr[i]

            if group[p] < group[q] or group[min(p+t, n)] < group[min(q+t, n)]:
                new_group[suffix_arr[i]] = new_group[suffix_arr[i-1]] + 1
            else:
                new_group[suffix_arr[i]] = new_group[suffix_arr[i-1]]

        group = new_group.copy()
        t *= 2
    return suffix_arr


user_string = str(input())
result_arr = get_suffix_arr(user_string)

print("접미사 배열")
for num in result_arr:
    print(num, end=" ")

print("\n")

print("정렬된 접미사 리스트")

for num in result_arr:
    print(user_string[num:])
