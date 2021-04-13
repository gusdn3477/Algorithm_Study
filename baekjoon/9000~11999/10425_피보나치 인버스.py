T = int(input())

fibo = [0] * 100001
fibo[0] = 0
fibo[1] = 1

for i in range(2, 100001):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

for i in range(T):
    t = int(input())

    idx = fibo.index(t)
    for j in range(idx + 1, 100001):
        if fibo[idx] == fibo[j]:
            idx = j

        elif fibo[idx] < fibo[j]:
            break

    print(idx)