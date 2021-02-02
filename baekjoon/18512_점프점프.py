a, b, c, d = map(int, input().split())
arr = []
arr2 = []
flag = 0

for i in range(101):
    arr.append(c + a * i)

for i in range(101):
    arr2.append(d + b * i)

for i in range(101):
    for j in range(101):
        if arr[i] == arr2[j]:
            print(arr[i])
            flag = 1
            break

    if arr[i] == arr2[j]:
        break

if flag == 0:
    print(-1)