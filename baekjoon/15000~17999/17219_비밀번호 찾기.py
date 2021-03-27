from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}

for i in range(N):
    a, b = stdin.readline().split()
    dic[a] = b

for i in range(M):
    a = stdin.readline().rstrip()
    print(dic[a])