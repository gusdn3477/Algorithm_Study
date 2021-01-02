N, K = map(int, input().split())
ct = 0
arr = [i for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if arr[j] != 0:
            save = arr[j]
            arr[j] = 0
            ct += 1

        if ct == K:
            break

    if ct == K:
        break

print(save)