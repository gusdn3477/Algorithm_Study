def bingo():
    global total
    total = 0
    # 가로 줄
    for i in range(5):
        ct = 0
        for j in range(5):
            if arr[i][j] == 0:
                ct += 1

        if ct == 5:
            total += 1

    # 세로 줄
    for i in range(5):
        ct = 0
        for j in range(5):
            if arr[j][i] == 0:
                ct += 1

        if ct == 5:
            total += 1

    # 대각선
    ct = 0
    for i in range(5):
        for j in range(5):
            if i == j and arr[i][j] == 0:
                ct += 1

        if ct == 5:
            total += 1

    ct = 0
    for i in range(5):
        for j in range(5):
            if i == 4 - j and arr[4 - j][j] == 0:
                ct += 1

        if ct == 5:
            total += 1

    if total >= 3:
        return True

    else:
        return False


def change(a):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == a:
                arr[i][j] = 0
                return


arr = []
ans = []
bing_cnt = 0
total = 0
ct = 0
for i in range(5):
    arr.append(list(map(int, input().split())))

for i in range(5):
    ans.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        ct += 1
        change(ans[i][j])

        if bingo():
            break

    if bingo():
        break

print(ct)