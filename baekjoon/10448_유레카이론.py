N = [i * (i + 1) // 2 for i in range(1, 100001)]
M = int(input())
flag = 0

for x in range(M):

    k = int(input())
    flag = 0
    for i in range(40):
        for j in range(i, 40):
            for z in range(j, 40):
                if N[i] + N[j] + N[z] == k:
                    flag = 1
                    break

    print(flag)