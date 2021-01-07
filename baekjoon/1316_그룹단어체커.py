N = int(input())
ct = 0

for i in range(N):

    stack = []
    flag = 0
    st = input()

    for i in range(len(st)):

        if not stack:
            stack.append(st[i])

        else:
            if stack[-1] == st[i]:
                continue

            else:
                stack.append(st[i])

    for i in range(len(stack)):
        if stack.count(stack[i]) > 1:
            flag = 1
            break

    if flag == 0:
        ct += 1

print(ct)