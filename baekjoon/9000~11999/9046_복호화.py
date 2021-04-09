N = int(input())

for i in range(N):
    dic = {}
    a = input().split()

    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] not in dic:
                dic[a[x][y]] = 1

            else:
                dic[a[x][y]] += 1

    arr = list(dic.items())
    arr = sorted(arr, key=lambda x: x[1], reverse=True)

    if len(arr) != 1:
        if arr[0][1] == arr[1][1]:
            print('?')

        else:
            print(arr[0][0])

    else:
        print(arr[0][0])