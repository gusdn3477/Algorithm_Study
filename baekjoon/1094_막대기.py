X = int(input())
arr = [64]

while sum(arr) != X:

    if sum(arr) > X:
        a = arr.pop()
        arr.append(a // 2)

        if sum(arr) < X:
            arr.append(a // 2)

print(len(arr))