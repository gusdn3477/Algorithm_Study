N = int(input())

for i in range(N):
    a,b = map(int, input().split())
    st = f'You get {a//b} piece(s) and your dad gets {a%b} piece(s).'
    print(st)