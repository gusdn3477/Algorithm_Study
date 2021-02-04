N, M = map(int, input().split())

pattern = 'WBWBWBWB'
pattern2 = 'BWBWBWBW'

map1 = []
map2 = []

for i in range(8):
    if i % 2 == 0:
        map1.append(pattern)
    else:
        map1.append(pattern2)

for i in range(8):
    if i % 2 == 0:
        map2.append(pattern2)
    else:
        map2.append(pattern)

board = []
wrong = 0
wrong2 = 0
min_wrong = 2500

for i in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        wrong = 0
        wrong2 = 0
        for a in range(8):
            for b in range(8):
                if board[i + a][j + b] != map1[a][b]:
                    wrong += 1

        for a in range(8):
            for b in range(8):
                if board[i + a][j + b] != map2[a][b]:
                    wrong2 += 1

        min_wrong = min(min_wrong, wrong, wrong2)

print(min_wrong)