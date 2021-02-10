N = int(input())
cow = {}
ct = 0

for i in range(N):
    a, b = map(int, input().split())

    if a not in cow:
        cow[a] = b

    else:
        if cow[a] != b:
            cow[a] = b
            ct += 1

print(ct)