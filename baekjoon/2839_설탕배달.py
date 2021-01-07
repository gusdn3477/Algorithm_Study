N = int(input())
arr = []
flag = 0

for i in range(N // 5, -1, -1):
    for j in range(N // 3, -1, -1):
        if i * 5 + j * 3 == N:
            flag = 1
            break

    if flag == 1:
        break

if flag == 0:
    print(-1)

else:
    print(i + j)