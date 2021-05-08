from math import sqrt

arr = [0] * 3001
arr[0] = 1
arr[1] = 1

for i in range(2, int(sqrt(3001)) + 1):
    for j in range(i + i, 3001, i):
        if arr[j] == 0:
            arr[j] = 1


def solution(nums):
    answer = 0

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for z in range(j + 1, len(nums)):
                if arr[nums[i] + nums[j] + nums[z]] == 0:
                    answer += 1

    return answer