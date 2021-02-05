N, M = map(int, input().split())
arr = []
max_len = 0

for i in range(N):
    arr.append(list(input()))

for i in range(N):
    for j in range(M):
        for k in range(min(N, M)):
            if i + k >= N or j + k >= M:
                continue

            if arr[i][j] == arr[i][j + k] and arr[i][j] == arr[i + k][j] and arr[i][j] == arr[i + k][j + k]:
                max_len = max(max_len, k + 1)

print(max_len ** 2)