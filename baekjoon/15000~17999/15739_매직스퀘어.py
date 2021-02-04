N = int(input())
arr = []
ar = []
check = True
for i in range(N):
    arr.append(list(map(int, input().split())))

perfect = [i for i in range(1, N * N + 1)]
total = N * (N ** 2 + 1) // 2

for i in range(N):
    for j in range(N):
        ar.append(arr[i][j])

ar = list(set(ar))
ar.sort()

if perfect != ar:
    check = False

if check == True:
    for i in range(N):
        a = sum(arr[i])
        if a != total:
            check = False

if check == True:
    for i in range(N):
        a = 0
        for j in range(N):
            a += arr[j][i]

        if a != total:
            check = False
            break

if check == True:
    a = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                a += arr[i][j]

    if a != total:
        check = False

if check == True:
    a = 0
    for i in range(N):
        for j in range(N - 1, -1, -1):
            if i == j:
                a += arr[i][j]

    if a != total:
        check = False

if check:
    print("TRUE")

else:
    print("FALSE")