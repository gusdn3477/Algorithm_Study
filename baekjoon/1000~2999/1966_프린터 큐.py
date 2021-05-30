T = int(input())

for i in range(T):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = []
    ct = 0

    for i in range(len(arr)):
        ans.append((arr[i], i))

    while True:

        flag = 0
        k = ans.pop(0)
        for i in range(len(ans)):
            if k[0] < ans[i][0]:
                ans.append(k)
                flag = 1
                break

        if flag == 0:

            if k[1] == M:
                ct += 1
                print(ct)
                break

            else:
                ct += 1