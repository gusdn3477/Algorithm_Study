arr = list(map(int, input().split()))
arr.sort()

start = arr[0]

while True:

    ct = 0
    flag = 0

    for i in range(len(arr)):
        if start % arr[i] == 0:
            ct += 1

        if ct >= 3:
            flag = 1
            break

    if flag == 1:
        break

    start += 1

print(start)