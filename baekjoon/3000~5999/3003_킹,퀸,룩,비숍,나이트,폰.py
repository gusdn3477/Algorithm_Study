arr = list(map(int, input().split()))
arr2 = [1,1,2,2,2,8]
for i in range(len(arr)):
    print(arr2[i]-arr[i], end=' ')