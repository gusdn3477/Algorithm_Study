def binary_search():
    global total_cnt
    start = 0
    end = arr[-1]

    while start <= end:

        total = 0
        mid = (start + end) // 2

        for i in range(len(arr)):

            if arr[i] < mid:
                total += arr[i]

            else:
                total += mid

        if total > M:
            end = mid - 1

        else:
            start = mid + 1
            total_cnt = max(total_cnt, mid)


total_cnt = 0
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
binary_search()
print(total_cnt)