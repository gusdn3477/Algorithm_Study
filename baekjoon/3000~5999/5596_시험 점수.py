arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

if sum(arr) >= sum(arr2):
    print(sum(arr))

else:
    print(sum(arr2))