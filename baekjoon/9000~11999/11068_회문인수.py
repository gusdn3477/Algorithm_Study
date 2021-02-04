N = int(input())

for i in range(N):
    M = int(input())
    for i in range(2, 65):
        arr = []
        flag = 0
        a = M
        while a > 0:
            arr.append(a % i)
            a = a // i

        arr2 = list(reversed(arr))

        if arr == arr2:
            flag = 1
            break

    print(flag)