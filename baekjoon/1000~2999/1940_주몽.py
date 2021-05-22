N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
ct = 0
start, end = 0, len(arr) - 1

while start < end:

    if arr[start] + arr[end] == M:
        ct += 1
        start += 1
        end -= 1

    elif arr[start] + arr[end] > M:
        end -= 1

    else:
        start += 1

print(ct)