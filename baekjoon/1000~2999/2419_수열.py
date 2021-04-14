N = int(input())
arr = list(map(int, input().split()))
start = 0
ct = 1
ct_max = 0
ct_max2 = 0

for i in range(1, len(arr)):
    if arr[start] <= arr[i]:
        ct += 1
        start = i

    else:
        ct_max = max(ct_max, ct)
        start = i
        ct = 1

ct_max = max(ct_max, ct)
ct = 1
start = 0

for i in range(1, len(arr)):
    if arr[start] >= arr[i]:
        ct += 1
        start = i

    else:
        ct_max2 = max(ct_max2, ct)
        start = i
        ct = 1

ct_max2 = max(ct_max2, ct)
print(max(ct_max, ct_max2))