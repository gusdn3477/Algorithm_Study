N, C = map(int, input().split())
arr = [0] * (C + 2)
ct = 0

for i in range(N):
    a = int(input())
    for j in range(a, C + 1, a):
        if arr[j] == 0:
            arr[j] = 1
            ct += 1

        else:
            continue

print(ct)