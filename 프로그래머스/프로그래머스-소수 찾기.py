from itertools import permutations
from math import sqrt

arr = [0] * 10000001
arr[0] = 1
arr[1] = 1
for i in range(2, int(sqrt(10000000)) + 1):
    for j in range(i + i, 10000000, i):
        if arr[j] == 0:
            arr[j] = 1


def solution(numbers):
    answer = 0
    poc = []
    for i in range(1, len(numbers) + 1):
        a = list(permutations(numbers, i))

        for j in range(len(a)):
            total = 0
            for x in range(len(a[j])):
                total = total * 10 + int(a[j][x])
                poc.append(total)

    poc = list(set(poc))
    for i in poc:
        if arr[i] == 0:
            answer += 1
    return answer