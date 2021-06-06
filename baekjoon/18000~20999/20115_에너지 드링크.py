N = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(len(arr)-1):
    arr[-1] += arr[i] / 2

print(arr[-1])