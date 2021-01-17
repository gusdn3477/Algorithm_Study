arr = list(map(int, input().split()))
ct = 0

for i in arr:
    if i > 0:
        ct += 1

print(ct)