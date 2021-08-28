def solution(dartResult):
    answer = 0
    stack = []
    st = ''
    num = '0123456789'
    for i in dartResult:
        if i in num:
            st += i
        elif i == 'S':
            stack.append(int(st))
            st = ''
        elif i == 'D':
            stack.append(int(st)**2)
            st = ''
        elif i == 'T':
            stack.append(int(st)**3)
            st = ''
        elif i == '*':
            if len(stack) >= 2:
                stack[-1], stack[-2] = stack[-1] * 2, stack[-2] * 2
            else:
                stack[-1] *= 2
        elif i == '#':
            stack[-1] *= -1
            st = ''
    return sum(stack)