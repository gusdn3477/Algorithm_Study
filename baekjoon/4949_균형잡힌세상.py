a = input()

while a != '.':
    poc = []
    for i in range(len(a)):
        if a[i] == '(' or a[i] == '[':
            poc.append(a[i])

        if a[i] == ')':
            if not poc or poc[-1] != '(':
                poc.append(a[i])
                break

            if poc[-1] == '(':
                poc.pop()

        if a[i] == ']':
            if not poc or poc[-1] != '[':
                poc.append(a[i])
                break

            if poc[-1] == '[':
                poc.pop()

    if not poc:
        print("yes")
    else:
        print("no")

    poc.clear()
    a = input()