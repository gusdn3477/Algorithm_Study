N = int(input())
arr = list(map(int, input().split()))
M = 0
Y = 0

for i in arr:
    Y += i // 30 + 1
    M += i // 60 + 1

Y = Y * 10
M = M * 15

if Y == M:
    print('Y M', Y)

elif Y > M:
    print('M', M)

else:
    print('Y', Y)