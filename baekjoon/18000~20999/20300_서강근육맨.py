N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = 0

if len(arr) % 2 == 1:

    for i in range(len(arr)//2):
        M = max(arr[i] + arr[len(arr)-i-2], M)        

    M = max(M, arr[-1])

else:

    for i in range(len(arr)//2):
        M = max(arr[i] + arr[len(arr)-i-1], M)

print(M)