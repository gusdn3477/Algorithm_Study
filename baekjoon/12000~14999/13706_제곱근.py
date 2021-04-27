def binary_search(start, end, key):
    while start <= end:

        mid = (start + end) // 2

        if mid * mid == key:
            return mid

        elif mid * mid > key:
            end = mid - 1

        else:
            start = mid + 1

    return -1


N = int(input())
a = binary_search(1, N, N)
print(a)