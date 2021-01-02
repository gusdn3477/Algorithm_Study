T = int(input())
poc = []

for i in range(T):
    N = int(input())
    for j in range(N):
        name, year = input().split()
        year = int(year)
        poc.append((year, name))

    poc.sort(reverse=True)
    print(poc[0][1])
    poc = []