N = int(input())
ct = 0

for i in range(N):

    str = input()
    stack = []

    for j in range(len(str)):

        if not stack:
            stack.append(str[j])

        else:
            if stack[-1] == str[j]:
                stack.pop()

            else:
                stack.append(str[j])

    if not stack:
        ct += 1

print(ct)