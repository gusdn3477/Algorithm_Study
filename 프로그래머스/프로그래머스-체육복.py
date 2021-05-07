def solution(n, lost, reserve):
    answer = 0

    reserve, lost = list(set(reserve) - set(lost)), list(set(lost) - set(reserve))
    reserve.sort()
    lost.sort()

    for i in range(len(reserve)):

        if reserve[i] - 1 in lost:
            lost.remove(reserve[i] - 1)

        elif reserve[i] + 1 in lost:
            lost.remove(reserve[i] + 1)

    return n - len(lost)