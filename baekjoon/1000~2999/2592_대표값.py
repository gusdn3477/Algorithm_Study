N = 10
poc = []
m = 0

for i in range(N):
    poc.append(int(input()))

for i in range(N):
    if poc.count(poc[i]) > m:
        m = poc.count(poc[i])
        ans = poc[i]

print(sum(poc) // len(poc))
print(ans)