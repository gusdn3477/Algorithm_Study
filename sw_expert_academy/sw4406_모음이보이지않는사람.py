N = int(input())
dic = ['a', 'e', 'i', 'o', 'u']

for i in range(1, N + 1):
    a = input()

    for z in dic:
        a = a.replace(z, '')

    s = f'#{i} {a}'
    print(s)