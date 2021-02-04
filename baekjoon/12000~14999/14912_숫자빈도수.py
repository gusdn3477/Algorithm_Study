N, M = map(int, input().split())
ct = 0

for i in range(1, N + 1):
    a = str(i)
    ct += a.count(str(M))

print(ct)