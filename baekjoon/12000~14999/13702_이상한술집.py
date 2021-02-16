def binary_search():
    start = 0
    end = arr[-1]
    global total_cnt

    while start <= end:

        mid = (start + end) // 2
        total = 0

        for i in arr:
            total += i // mid

        if total < K:
            end = mid - 1

        else:
            start = mid + 1
            total_cnt = max(total_cnt, mid)


total_cnt = 0
N, K = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
binary_search()
print(total_cnt)