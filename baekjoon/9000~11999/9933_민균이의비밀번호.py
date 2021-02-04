N = int(input())
arr = []
flag = 0
a = 0
b = 0
for i in range(N):
    arr.append(input())

for i in range(N):
    flag = 0
    for j in range(N):
        if arr[i][::-1] in arr:
            a = len(arr[i])
            b = arr[i][a // 2]
            flag = 1
            break

    if flag == 1:
        break

print(a, b)