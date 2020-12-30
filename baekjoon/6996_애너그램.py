N = int(input())

for i in range(N):

    a, b = input().split()
    c = list(a)
    d = list(b)
    c.sort()
    d.sort()

    if c == d:
        print(a, '&', b, 'are anagrams.')

    else:
        print(a, '&', b, 'are NOT anagrams.')