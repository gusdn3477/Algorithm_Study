def binary_search(key):
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            start = mid + 1

        else:
            end = mid - 1

    return -1


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = binary_search(arr[len(arr) // 2 - 1])

print(arr[a])