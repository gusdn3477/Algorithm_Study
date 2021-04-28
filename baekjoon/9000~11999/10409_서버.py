n, T = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
ct = 0

for i in arr:

    if total + i > T:
        break

    else:
        total += i
        ct += 1

print(ct)