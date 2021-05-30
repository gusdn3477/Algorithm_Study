N = int(input())
cons = -1

for i in range(N + 1):

    tmp = i
    tmp_sum = i

    while tmp > 0:
        tmp_sum += tmp % 10
        tmp //= 10

    if tmp_sum == N:
        cons = i
        break

if cons == -1:
    print(0)

else:
    print(cons)