import heapq


def solution(n, works):
    answer = 0
    heap = []

    for i in works:
        heapq.heappush(heap, [-i, i])

    for i in range(n):
        a, b = heapq.heappop(heap)
        a += 1
        b -= 1

        if b < 0:
            b = 0

        heapq.heappush(heap, [a, b])

    while heap:
        a, b = heapq.heappop(heap)
        answer += b ** 2

    return answer