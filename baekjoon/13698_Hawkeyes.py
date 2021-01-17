arr = [1, 2, 3, 4]
a = input()

for i in a:
    if i == 'A':
        arr[0], arr[1] = arr[1], arr[0]

    elif i == 'B':
        arr[0], arr[2] = arr[2], arr[0]

    elif i == 'C':
        arr[0], arr[3] = arr[3], arr[0]

    elif i == 'D':
        arr[1], arr[2] = arr[2], arr[1]

    elif i == 'E':
        arr[1], arr[3] = arr[3], arr[1]

    elif i == 'F':
        arr[2], arr[3] = arr[3], arr[2]

print(arr.index(1) + 1)
print(arr.index(4) + 1)