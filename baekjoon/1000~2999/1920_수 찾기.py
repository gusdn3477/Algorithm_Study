def binary_search(start, end, key):
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] < key:
            start = mid + 1

        elif arr[mid] > key:
            end = mid - 1

        else:
            return mid

    return -1


N = int(input())
arr = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

for i in arr2:
    a = binary_search(0, len(arr) - 1, i)

    if a == -1:
        print(0)

    else:
        print(1)