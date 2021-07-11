def solution(nums):
    answer = 0
    ct = 0
    visited = [0] * 200001
    for i in range(len(nums)):
        if ct == len(nums) // 2:
            break
        if visited[nums[i]] == 0:
            visited[nums[i]] = 1
            answer += 1
            ct += 1
    return answer