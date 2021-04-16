T = int(input())

for i in range(T):
    a = int(input())
    total = 1
    dic = {}
    for j in range(a):
        a, b = input().split()

        if b not in dic:
            dic[b] = 1

        else:
            dic[b] += 1

    for k in dic.values():
        total *= (k + 1)

    print(total - 1)