N = int(input())
ct = 0
ct2 = 0

for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        ct += 1

    elif a < b:
        ct2 += 1

print(ct, ct2)