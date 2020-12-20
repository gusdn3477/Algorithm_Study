N, M = map(int, input().split())

graph = list(map(int, input().split()))

m = max(graph)

start = 0
end = m
p = 0

while start <= end:

    total = 0
    mid = (start + end) // 2

    for i in graph:
        if i > mid:
            total += i - mid

    if total >= M:
        p = mid
        start = mid + 1

    else:
        end = mid - 1

print(p)