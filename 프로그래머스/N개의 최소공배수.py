from collections import deque


def GCD(x, y):
    if x == 0:
        return y

    else:
        return GCD(y % x, x)


def solution(arr):
    answer = 0
    save = arr.pop(0)
    queue = deque(arr)

    while queue:
        a = queue.popleft()
        save = save * a // GCD(save, a)

    return save