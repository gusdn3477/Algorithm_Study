total = 0
m = 0
for i in range(10):
    a, b = map(int, input().split())
    total = total + b - a
    if total > m:
        m = total

print(m)