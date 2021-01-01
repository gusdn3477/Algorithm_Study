N, M = map(int, input().split())
st = ''
flag = 0

for i in range(N):
    st += str(N)

    if len(st) > M:
        flag = 1
        break

if flag == 0:
    print(st)

else:
    for i in range(M):
        print(st[i], end='')