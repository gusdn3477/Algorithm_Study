from sys import stdin

N, M = map(int, stdin.readline().split())
arr = []

for i in range(1, N + 1):
    arr.append(stdin.readline().rstrip())

for i in range(M):

    a = stdin.readline().rstrip()
    try:
        a = int(a)
        print(arr[a - 1])
    except:
        # 문자열인 경우
        print(arr.index(a) + 1)