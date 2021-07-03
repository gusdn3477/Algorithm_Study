def findAns(x):
    ans = 0
    for i in range(1,x+1):
        if x % i == 0:
            ans += 1
    return ans

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        t = findAns(i)
        if t % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer