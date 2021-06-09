def findStr(k):

    global ans

    for i in range(H):
        for j in range(W):
            if arr[i][j+k*W] != '?':
                ans += arr[i][j+k*W]
                return

    ans += '?'


N,H,W = map(int, input().split())

arr = []
ans = ''
for i in range(H):
    arr.append(input())

for i in range(N):
    findStr(i)

print(ans)