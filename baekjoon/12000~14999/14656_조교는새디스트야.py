N = int(input())
arr = [0]
ct = 0
arr.extend(list(map(int, input().split())))
for i in range(1, len(arr)):
    if i != arr[i]:
        ct += 1

print(ct)