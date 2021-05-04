N = int(input())
arr = []

for i in range(N):
    arr.append(input())

M = int(input())

if M == 1:

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end='')
        print()

elif M == 3:

    for i in range(N):
        for j in range(N):
            print(arr[N - i - 1][j], end='')
        print()

else:
    for i in range(N):
        for j in range(N):
            print(arr[i][N - j - 1], end='')
        print()