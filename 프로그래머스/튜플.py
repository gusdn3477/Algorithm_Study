def solution(s):
    answer = []
    ans = []
    a = []
    s = s[1:]
    s = s[:-1]
    st = ''
    flag = 0
    
    for i in s:
        if i == '}':
            if not ans:
                ans.append(int(st))
                answer.append(ans)
            else:
                ans.append(int(st))
                answer.append(ans)
            st = ''
            ans = []
        elif i.isdecimal():
            st += i
        elif st and i == ',':
            ans.append(int(st))
            st = ''
    answer.sort(key = lambda x : len(x))
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if answer[i][j] not in a:
                a.append(answer[i][j])
    return a