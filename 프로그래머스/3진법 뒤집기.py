def solution(n):
    answer = 0
    arr = []
    ct = 0
    while n:
        arr.append(n%3)
        n //= 3
    for i in range(len(arr)-1,-1,-1):
        answer += arr[i] * 3 ** ct
        ct += 1
    return answer