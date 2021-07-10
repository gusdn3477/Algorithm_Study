def solution(number, k):
    stack = []
    
    for i in range(len(number)):
        a = int(number[i])
        if not stack:
            stack.append(str(a))
        else:
            flag = 0
            while a > int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
                if not stack:
                    break
            stack.append(str(a))
    for i in range(k):
        stack.pop()
    return ''.join(stack)