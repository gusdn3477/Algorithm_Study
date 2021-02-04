N = int(input())
F = int(input())

M = (N // 100) * 100

for i in range(100):
    if (M + i) % F == 0:
        m = str(M + i)
        break

print(m[-2:])