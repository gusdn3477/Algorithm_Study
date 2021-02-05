koong = [0] * 68
koong[0] = 1
koong[1] = 1
koong[2] = 2
koong[3] = 4

for i in range(4, 68):
    koong[i] = koong[i - 1] + koong[i - 2] + koong[i - 3] + koong[i - 4]

N = int(input())
for i in range(N):
    a = int(input())
    print(koong[a])