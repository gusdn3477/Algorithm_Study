N = int(input())
M = int(input())
arr = list(map(int, input().split()))
album = []

for i in arr:

    # 시간 추가해주기
    for j in range(len(album)):
        album[j][2] += 1

    # 두번째 요소가 추천횟수, 세번째 요소가 시간
    if len(album) < N:
        flag = 1
        for j in range(len(album)):
            if album[j][0] == i:
                flag = 0
                album[j][1] += 1

        if flag:
            album.append([i, 1, 0])

    else:
        # 일단 정렬
        flag = 1
        for j in range(len(album)):

            if album[j][0] == i:
                album[j][1] += 1
                flag = 0
                break

        if flag:
            album = sorted(album, key=lambda x: (x[1], -x[2]))
            album.pop(0)
            album.append([i, 1, 0])

album.sort()
for i in album:
    print(i[0], end=' ')