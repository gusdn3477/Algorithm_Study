N = list(map(int, input()))
M = N[::-1]
total = 0
M.sort(reverse=True)

for i in M:
    total = total * 10 + i

s = sum(N)

if s % 3 == 0 and total % 10 == 0:
    print(total)

else:
    print(-1)