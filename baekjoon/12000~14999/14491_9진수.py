T = int(input())
N = []
while T > 0:
    N.append(T % 9)
    T = T // 9

for i in range(len(N) - 1, -1, -1):
    print(N[i], end='')