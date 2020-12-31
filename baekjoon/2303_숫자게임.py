# 4중 for문으로 풀리는 게 함정.

N = int(input())
poc = []

for i in range(N):
    poc.append(list(map(int, input().split())))

m = 0
win = 0
for i in range(N):
    for j in range(len(poc[0])):
        for z in range(j + 1, len(poc[0])):
            for k in range(z + 1, len(poc[0])):
                if (poc[i][j] + poc[i][z] + poc[i][k]) % 10 >= m:
                    m = (poc[i][j] + poc[i][z] + poc[i][k]) % 10
                    win = i + 1

print(win)