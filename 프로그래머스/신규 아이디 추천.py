def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalpha() or i.isdecimal() or i =='-' or i == '_' or i == '.':
            answer += i
    ans = ''
    for i in answer:
        if not ans:
            ans += i
        elif ans[-1] == '.' and i == '.':
            continue
        else:
            ans += i
            
    answer = ans
    if answer:
        if answer[0] == '.':
            answer = answer[1:]
    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]
    if not answer:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        answer = answer + (3 - len(answer)) * answer[-1]
    return answer