A = list(map(int, input().split()))
ans = 0

for i in A:
    ans += (i ** 2) % 10

print(ans % 10)