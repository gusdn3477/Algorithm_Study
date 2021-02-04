from sys import stdin

N = int(stdin.readline())

for i in range(1,N+1):
    a,b = map(int, stdin.readline().split())
    print('Case #%d: %d + %d = %d' %(i,a,b,a+b))