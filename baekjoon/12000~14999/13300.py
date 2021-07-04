import math

N, K = map(int, input().split())
people = [[0 for i in range(7)] for j in range(2)]
room = 0
for i in range(N):
    a, b = map(int, input().split())
    people[a][b] += 1

for i in range(2):
    for j in range(1,7):
        room += math.ceil(people[i][j] / K)
print(room)