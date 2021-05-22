N = int(input())
arr = list(map(int, input().split()))
M = int(input())
total = 0
ct = 0
start = 0
end = len(arr) - 1
arr.sort()

while start < end:

    if arr[start] + arr[end] == M:
        ct += 1

    if arr[start] + arr[end] >= M:
        end -= 1

    else:
        start += 1

print(ct)