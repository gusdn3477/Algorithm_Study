arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
total = 0
total2 = 0
flag = 0

for i in range(9):

    total += arr[i]

    if total > total2:  # 이기고 있음
        flag = 1

    if total < total2 and flag == 1:
        flag = 2

    total2 += arr2[i]

    if total > total2:  # 이기고 있음
        flag = 1

    if total < total2 and flag == 1:
        flag = 2

if flag == 2:
    print('Yes')

else:
    print('No')