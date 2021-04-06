def _print():
    for i in arr:
        print(i, end=' ')
    print()


arr = list(map(int, input().split()))

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            _print()