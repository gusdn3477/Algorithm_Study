N = int(input())
arr = []
total = 0

for i in range(1, N + 1):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(0, len(arr)):

    tip = arr[i] - i

    if tip >= 0:
        total += tip

print(total)