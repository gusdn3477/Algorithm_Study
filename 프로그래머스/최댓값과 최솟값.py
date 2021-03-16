def solution(s):
    answer = ''
    arr = s.split(' ')
    arr = list(map(int, arr))
    answer += str(min(arr))
    answer += ' '
    answer += str(max(arr))

    return answer