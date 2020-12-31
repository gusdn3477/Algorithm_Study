N, M = map(int, input().split())
poc = list(map(int, input().split()))
ct = 0
for i in range(len(poc)):
    total = 0
    for j in range(i, len(poc)):
        total += poc[j]

        if total == M:
            ct += 1
        elif total > M:
            break

print(ct)