def binary_search(key):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] < key:
            start = mid + 1

        elif arr[mid] > key:
            end = mid - 1

        else:
            return mid

    return -1


T = int(input())

for i in range(T):

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    M = int(input())
    arr2 = list(map(int, input().split()))

    for j in arr2:
        a = binary_search(j)
        if a == -1:
            print(0)

        else:
            print(1)