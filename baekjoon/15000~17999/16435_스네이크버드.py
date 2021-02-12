N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in arr:
    if L >= i:
        L += 1

print(L)