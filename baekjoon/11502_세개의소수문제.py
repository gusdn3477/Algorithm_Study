from math import sqrt

a = [0] * 1001
a[0] = 1
a[1] = 1

for i in range(2, int(sqrt(1000)) + 1):
    for j in range(i + i, 1001, i):
        if a[j] == 0:
            a[j] = 1

N = int(input())
for i in range(N):
    M = int(input())
    flag = 0
    for d in range(2, 1001):
        for b in range(2, 1001):
            for c in range(2, 1001):
                if a[d] == 0 and a[b] == 0 and a[c] == 0:
                    if b + d + c == M:
                        print(d, b, c)
                        flag = 1
                        break

                if flag == 1:
                    break

            if flag == 1:
                break

        if flag == 1:
            break