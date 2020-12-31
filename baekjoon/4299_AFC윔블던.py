N, M = map(int, input().split())
flag = 0

for i in range(0, 1000):
    for j in range(0, 1000):
        if i + j == N and abs(i - j) == M:
            a = i
            b = j
            flag = 1
            break

if flag == 0:
    print(-1)

else:
    if a > b:
        print(a, b)

    else:
        print(b, a)