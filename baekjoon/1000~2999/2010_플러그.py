N = int(input())
total = 0

for i in range(N):

    a = int(input())

    if i == N - 1:
        break

    total += a - 1

print(total + a)