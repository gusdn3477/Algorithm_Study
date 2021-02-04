N = int(input())
total = 0

for i in range(N):
    a, b = map(int, input().split())
    total += b % a

print(total)