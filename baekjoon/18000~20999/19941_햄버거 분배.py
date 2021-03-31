N, K = map(int, input().split())
arr = list(input())
total = 0

for i in range(len(arr)):

    if arr[i] == 'P':
        for j in range(i - K, i + K + 1):

            if j < 0 or j >= N:
                continue

            if arr[j] == 'H':
                arr[j] = 'C'
                total += 1
                break

print(total)