N = int(input())
arr = list(map(int, input().split()))
line = []

for i in range(len(arr)):

    if i == 0:
        line.append(1)

    elif i == 1:
        if arr[1] == 0:
            line.append(2)

        else:
            line.insert(0, 2)

    else:
        line.insert(len(line) - arr[i], i + 1)

for i in line:
    print(i, end=' ')