N = int(input())
arr = list(map(int, input().split()))
total = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        total += abs(arr[i] - arr[j])

print(total)