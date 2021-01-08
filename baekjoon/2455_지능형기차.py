total = 0
m = 0
for i in range(4):
    a, b = map(int, input().split())
    total += b - a

    m = max(m, total)

print(m)