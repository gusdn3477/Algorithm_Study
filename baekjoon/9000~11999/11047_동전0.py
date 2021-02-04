N, K = map(int, input().split())
poc = []
ct = 0

for i in range(N):
    poc.append(int(input()))

poc.sort(reverse=True)

for i in range(len(poc)):

    if K // poc[i] != 0:
        ct += K // poc[i]
        K = K % poc[i]

print(ct)